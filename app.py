import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain


load_dotenv()


# title quantum computing chatbot
st.title("Quantum Computing Chatbot")

file_path = "QUANTUM COMPUTING.pdf"
loader = PyPDFLoader(file_path)
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter( chunk_size=1000)
docs = text_splitter.split_documents(data)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store=Chroma.from_documents(embedding=embeddings, documents=docs, persist_directory="./chroma_db")
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 10})

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.3,
    max_tokens=512,

)

query = st.chat_input("Ask a question about quantum computing:")

system_prompt = (
    "You are a helpful assistant that provides information about quantum computing. "
    "You will be provided with some documents and you will answer the user's question based on those documents. "
    "If you don't know the answer, say 'I don't know'. "
    "If the answer is not in the documents, say 'I don't know'. "
    "If the answer is in the documents, provide a detailed answer. "
    "Be concise and clear. "
    "You can use the information from the documents.\n\n"
    "The documents are: {context}"
)

if query:
    prompt=ChatPromptTemplate.from_messages(
    [
    ("system",system_prompt),
    ("human","{input}")
    ]
)
    chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, chain)
    response = retrieval_chain.invoke({"input": query})
    st.write(response["answer"])