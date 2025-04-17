# 🧠 Quantum Computing Chatbot
This project is an AI-powered chatbot that answers questions about Quantum Computing using the contents of a PDF document. It processes the document, stores it as embeddings, and uses a retrieval-based method to respond to user queries via a conversational interface.

## 🚀 Features
- Loads and analyzes a PDF document

- Uses Google's Gemini 1.5 Pro model for natural language understanding

- Implements a retrieval-augmented generation (RAG) pipeline with LangChain

- Simple and interactive UI with Streamlit

##  🛠️ Installation
### 1. Install Dependencies
```
pip install streamlit langchain langchain-community langchain-core \
            langchain-google-genai chromadb python-dotenv
```
### 2. Environment Variables
Create a .env file in your project directory and add your Google API key:
```
GOOGLE_API_KEY=your_google_api_key_here
```
### 3. Add the PDF File
Place your pdf file in the project root directory. This will be the knowledge source for the chatbot.

## ▶️ Running the App
```
streamlit run app.py
```
## 📁 Project Structure
```
.
├── app.py
├── .env
├── QUANTUM COMPUTING.pdf
└── chroma_db/
```

## 💬 How to Use
1. Enter a question related to quantum computing in the chat input.
2. The bot will retrieve relevant context from the document and respond.
3. If the answer is not found in the document, it will say "I don't know".

## 🧰 Tech Stack
- LangChain
- Google Generative AI (Gemini)
- Streamlit
- Chroma Vector DB

## 📜 License
This is a sample educational project. Feel free to modify and build upon it for your own use.🧡
