from flask import Flask
import os
import textwrap
import google.generativeai as genai

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA


def load_and_split_pdf(pdf_path):
    pdf_loader = PyPDFLoader(pdf_path)
    return pdf_loader.load_and_split()


def setup_gemini_model(model_name, api_key, temperature):
    return ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key, temperature=temperature, convert_system_message_to_human=True)


def create_embeddings_and_index(texts, model_name, api_key):
    embeddings = GoogleGenerativeAIEmbeddings(model=model_name, google_api_key=api_key)
    vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":5})
    return vector_index


def create_rag_qa_chain(model, vector_index):
    return RetrievalQA.from_chain_type(model, retriever=vector_index, return_source_documents=True)

GOOGLE_API_KEY=''

PDF_PATH = "./ppcbcc.pdf"
GEMINI_MODEL_NAME = "gemini-pro"
EMBEDDING_MODEL_NAME = "models/embedding-001"
TEMPERATURE = 0.2
CHUNK_SIZE = 700
CHUNK_OVERLAP = 100

pages = load_and_split_pdf(PDF_PATH)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
context = "\n\n".join(str(p.page_content) for p in pages)
texts = text_splitter.split_text(context)
gemini_model = setup_gemini_model(GEMINI_MODEL_NAME, GOOGLE_API_KEY, TEMPERATURE)
vector_index = create_embeddings_and_index(texts, EMBEDDING_MODEL_NAME, GOOGLE_API_KEY)
qa_chain = create_rag_qa_chain(gemini_model, vector_index)

question = "Como deve ser calculada a nota final de TCC II?"
result = qa_chain({"query": question})
print("Resposta:", result["result"])

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>"+result["result"]+"</p>"