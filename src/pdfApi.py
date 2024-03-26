import os
import textwrap
import google.generativeai as genai

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA


class PdfApi:
    def __init__(self, pdfName="ppcbcc.pdf"):
        self.pdfPathName = "./src/pdfs/"+pdfName
        self.GOOGLE_API_KEY='AIzaSyAIqN74c-rDNx-zQGv62PRvsI5Cd5NBZ5Q'
        self.GEMINI_MODEL_NAME = "gemini-pro"
        self.EMBEDDING_MODEL_NAME = "models/embedding-001"
        self.TEMPERATURE = 0.2
        self.CHUNK_SIZE = 700
        self.CHUNK_OVERLAP = 100

    def load_and_split_pdf(self, pdf_path):
        pdf_loader = PyPDFLoader(pdf_path)
        return pdf_loader.load_and_split()

    def setup_gemini_model(self, model_name, api_key, temperature):
        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=api_key,
            temperature=temperature,
            convert_system_message_to_human=True,
        )

    def create_embeddings_and_index(self, texts, model_name, api_key):
        embeddings = GoogleGenerativeAIEmbeddings(
            model=model_name, google_api_key=api_key
        )
        vector_index = Chroma.from_texts(texts, embeddings).as_retriever(
            search_kwargs={"k": 5}
        )
        return vector_index

    def create_rag_qa_chain(self, model, vector_index):
        return RetrievalQA.from_chain_type(
            model, retriever=vector_index, return_source_documents=True
        )
    
    def path_exist(self):
         local = "./src/pdfs"

         if os.path.isdir(local):
            # Lista os itens no diretório
            directory_contents = os.listdir(local)
            
            # Mostra os itens
            print(f"Conteúdo da pasta '{local}':")
            for item in directory_contents:
                print(item)
         else:
            print(f"O caminho especificado '{local}' não é um diretório.")

    def pdf_response(self, question: str) -> str:

        pages = self.load_and_split_pdf(self.pdfPathName)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.CHUNK_SIZE, chunk_overlap=self.CHUNK_OVERLAP)
        context = "\n\n".join(str(p.page_content) for p in pages)
        texts = text_splitter.split_text(context)
        gemini_model = self.setup_gemini_model(self.GEMINI_MODEL_NAME, self.GOOGLE_API_KEY, self.TEMPERATURE)
        vector_index = self.create_embeddings_and_index(texts, self.EMBEDDING_MODEL_NAME, self.GOOGLE_API_KEY)
        qa_chain = self.create_rag_qa_chain(gemini_model, vector_index)

        result = qa_chain({"query": question})

        return result