import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from htmlTemplates import css, bot_template, user_template
import google.generativeai as genai

# === Load .env ===
load_dotenv()

# === Configure Gemini API ===
def get_llm():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    return genai.GenerativeModel("gemini-2.5-pro")

# === Extract PDF text ===
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

# === Chunk text ===
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    return text_splitter.split_text(text)

# === Vector store ===
def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings()
    vectorstore = Chroma.from_texts(
        texts=text_chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    return vectorstore

# === Gemini Q&A ===
def handle_userinput(user_question):
    model = get_llm()
    retriever = st.session_state.vectorstore.as_retriever()
    relevant_chunks = retriever.get_relevant_documents(user_question)

    context = "\n".join([doc.page_content for doc in relevant_chunks])
    prompt = f"You are a helpful assistant. Use the following context to answer the question.\n\n{context}\n\nQuestion: {user_question}"

    response = model.generate_content(prompt)

    # ⬇️ Insert newest Q&A at top
    st.session_state.chat_history.insert(0, {"role": "user", "content": user_question})
    st.session_state.chat_history.insert(0, {"role": "assistant", "content": response.text})

    # 💬 Display from latest to oldest
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(user_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)
        else:
            st.markdown(bot_template.replace("{{MSG}}", message["content"]), unsafe_allow_html=True)

# === Main app ===
def main():
    st.set_page_config(
        page_title="KnowledgeHub",
        page_icon="📘",
        layout="wide"
    )

    st.markdown(css, unsafe_allow_html=True)

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None

    st.title("📘 KnowledgeHub – Smart PDF Assistant")
    user_question = st.text_input("🔍 Ask a question about your uploaded documents:")
    if user_question and st.session_state.vectorstore:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("📂 Upload Your PDFs")
        pdf_docs = st.file_uploader("Drag and drop PDF files here", accept_multiple_files=True)
        if st.button("📎 Process"):
            with st.spinner("Reading and indexing documents..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.vectorstore = vectorstore
                st.success("✅ Documents processed successfully!")

if __name__ == '__main__':
    main()
