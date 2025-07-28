# 📘 KnowledgeHub – Smart PDF Assistant

KnowledgeHub is an AI-powered Streamlit application that allows users to upload PDF documents and ask questions. It uses **Google Gemini Pro** for answering questions based on content extracted from uploaded PDFs, with **LangChain**, **HuggingFace embeddings**, and **Chroma** as the vector store.

---

## 🚀 Features

- 📂 Upload and process multiple PDF documents  
- 🤖 Ask questions based on document content  
- 🧠 Uses `HuggingFaceEmbeddings` + `Chroma` for vector search  
- 🔎 Fast and relevant answers using `Google Gemini`  
- 🧾 Clean, professional, and responsive UI  
- 🧠 Shows the **most recent question-answer first**  
- ☁️ Smart document chunking and persistent vector store

---

## 📸 Demo

> Upload your PDFs on the sidebar  
> Ask a question like _"What is the summary of chapter 3?"_

![App Screenshot](https://github.com/didula08/KnowledgeHub-RAG/assets/demo.png) *(replace with actual screenshot)*

---

## 🧰 Tech Stack

| Layer           | Technology                                  |
|----------------|----------------------------------------------|
| 💻 Frontend     | Streamlit + HTML/CSS                        |
| 🧠 Embeddings   | HuggingFace (`all-mpnet-base-v2`)          |
| 📁 Vector Store | Chroma DB                                   |
| 🤖 LLM          | Google Gemini Pro via `google.generativeai` |
| 🧾 PDF Parsing  | PyPDF2                                      |

---

## 📂 Project Structure

KnowledgeHub-RAG/
│
├── app.py # Main Streamlit application
├── htmlTemplates.py # UI styling & message templates
├── requirements.txt # All Python dependencies
├── .env # (Not pushed) API key storage
├── .gitignore # Ignore venv, .env, chroma_db
├── chroma_db/ # Vector DB (excluded from Git)
├── venv/ # Virtual environment (excluded)
└── README.md


---

## 🔐 Environment Setup

1. Rename `.env.example` to `.env` and add your Gemini API key:
GEMINI_API_KEY=your_google_gemini_key


2. Install required Python packages:
```bash
pip install -r requirements.txt

▶️ Run the App
bash
Copy
Edit
streamlit run app.py

📦 Dependencies
txt
Copy
Edit
streamlit
langchain
langchain-community
chromadb
google-generativeai
PyPDF2
python-dotenv
sentence-transformers

