css = """
<style>
.chat-message {
    padding: 1.25rem;
    border-radius: 0.75rem;
    margin-bottom: 1.5rem;
    display: flex;
    align-items: flex-start;
    gap: 1.25rem;
    box-shadow: 0px 4px 18px rgba(0, 0, 0, 0.25);
    background: #1e293b;
    border-left: 4px solid #3b82f6;
}

.chat-message.user {
    background: linear-gradient(to right,#0f172a, #1e293b);
}

.chat-message.bot {
    background: linear-gradient(to right, #0f172a, #1e293b);
}

.chat-message .avatar {
    flex-shrink: 0;
    padding-top: 4px;
}

.chat-message .avatar img {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #ffffff44;
    box-shadow: 0px 0px 12px rgba(255, 255, 255, 0.1);
}

.chat-message .message {
    flex-grow: 1;
    color: #f8fafc;
    font-size: 1rem;
    line-height: 1.6;
    font-weight: 400;
    white-space: pre-wrap;
}
</style>
"""

# 🤖 Professional Bot Avatar
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

# 👤 Professional User Avatar
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/1144/1144760.png" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
