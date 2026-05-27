🤖 SynapseChat AI
SynapseChat AI is an intelligent conversational chatbot built using Streamlit, HuggingFace Transformers, and the Wikipedia API. It provides smart, context-aware responses with a modern ChatGPT-like interface.

🚀 Features
💬 ChatGPT-style conversational UI using Streamlit
🧠 AI-powered responses using HuggingFace Transformers
📚 Wikipedia integration for factual answers
⚡ Fast and lightweight architecture
🗂️ Session-based chat memory
🎨 Modern dark-themed UI
🌐 Ready for deployment (Streamlit Cloud / Render)
🛠️ Tech Stack
Python 🐍
Streamlit 🎈
HuggingFace Transformers 🤗
Wikipedia API 📖
PyTorch 🔥
📁 Project Structure (Folder Architecture)
,,,
SynapseChat-AI/
│
├── app.py                  # Main Streamlit application (UI layer)
├── model.py               # AI logic (HuggingFace + Wikipedia processing)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── assets/                # Static files (images, logos, banners)
│   ├── logo.png           # SynapseChat logo
│   └── banner.png         # GitHub banner (optional)
│
├── utils/                 # Helper functions (optional expansion)
│   └── helpers.py
│
└── .gitignore             # Files to ignore in GitHub
,,

📸 UI Preview
<img width="1915" height="963" alt="image" src="https://github.com/user-attachments/assets/5bc036c8-a14b-4fa3-b510-4a6f760d40b8" />
<img width="1899" height="901" alt="image" src="https://github.com/user-attachments/assets/8d223cdf-5220-46e9-9bda-56938761bb43" />


📌 How It Works
User enters a query in the chat interface
Input is processed by the AI model (model.py)
If needed, Wikipedia API fetches factual context
AI generates a response
Response is displayed in Streamlit UI
📦 Installation
# Clone the repository
git clone https://github.com/your-username/synapsechat-ai.git

# Move into project directory
cd synapsechat-ai

# Install dependencies
pip install -r requirements.txt
▶️ Run the App
streamlit run app.py
🚀 Future Improvements
🔐 User authentication system
🧠 Long-term memory database integration
🤖 Upgrade to advanced LLMs (Mistral / LLaMA / GPT APIs)
🌐 Custom domain deployment
🎤 Voice input/output support
📊 Analytics dashboard for chats
