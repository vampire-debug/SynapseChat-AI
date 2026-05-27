import streamlit as st
from model import get_response

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Custom CSS (ChatGPT-like UI)
# -----------------------------
st.markdown("""
<style>
/* Background */
.main {
    background-color: #0e1117;
    color: white;
}

/* Chat bubbles */
.user-msg {
    background: linear-gradient(135deg, #2b7cff, #1a5cff);
    color: white;
    padding: 12px 16px;
    border-radius: 18px;
    margin: 8px 0;
    max-width: 75%;
    margin-left: auto;
    text-align: left;
}

.bot-msg {
    background: #1f2937;
    color: #e5e7eb;
    padding: 12px 16px;
    border-radius: 18px;
    margin: 8px 0;
    max-width: 75%;
    margin-right: auto;
}

/* Chat container */
.chat-container {
    padding: 20px;
    max-width: 900px;
    margin: auto;
}

/* Title */
h1 {
    text-align: center;
    color: #ffffff;
}

/* Input box fix */
.stChatInputContainer {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 60%;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("🤖 AI Chatbot using HuggingFace + Streamlit")

# -----------------------------
# Header
# -----------------------------
st.title("🤖 SynapseChat AI")
st.caption("ChatGPT-style UI with improved design")

# -----------------------------
# Chat display
# -----------------------------
chat_container = st.container()

with chat_container:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-msg'>🧑‍💻 {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-msg'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

# -----------------------------
# Input
# -----------------------------
user_input = st.chat_input("Ask me anything...")

if user_input:
    # store user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # get AI response
    response = get_response(user_input)

    # store bot message
    st.session_state.messages.append({"role": "bot", "content": response})

    st.rerun()
