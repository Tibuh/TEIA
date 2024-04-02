import warnings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

class PdfApi:
    def __init__(self, pdfName="ppcbcc.pdf"):
        warnings.filterwarnings("ignore")
        self.pdfPathName = "./src/pdfs/"+pdfName
        self.GOOGLE_API_KEY='AIzaSyAIqN74c-rDNx-zQGv62PRvsI5Cd5NBZ5Q'
        self.GEMINI_MODEL_NAME = "gemini-pro"
        self.EMBEDDING_MODEL_NAME = "models/embedding-001"
        self.TEMPERATURE = 0.5975
        self.CHUNK_SIZE = 20000
        self.CHUNK_OVERLAP = 2000
        self.TEMPLATE = """Use os fragmentos de contexto a seguir para responder a questão no final.Deixe a resposta o mais concisa possível. Sempre diga "obrigado por perguntar!" no final da resposta. 
				{context}
				Question: {question}
				Helpful Answer:"""

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
        QA_CHAIN_PROMPT = PromptTemplate.from_template(self.TEMPLATE)
        return RetrievalQA.from_chain_type(
            model, retriever=vector_index, return_source_documents=True,
            chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
        )
    

    def pdf_response(self, question: str) -> str:
        pages = self.load_and_split_pdf(self.pdfPathName)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.CHUNK_SIZE, chunk_overlap=self.CHUNK_OVERLAP)
        context = "\n\n".join(str(p.page_content) for p in pages)
        texts = text_splitter.split_text(context)
        gemini_model = self.setup_gemini_model(self.GEMINI_MODEL_NAME, self.GOOGLE_API_KEY, self.TEMPERATURE)
        vector_index = self.create_embeddings_and_index(texts, self.EMBEDDING_MODEL_NAME, self.GOOGLE_API_KEY)
        qa_chain = self.create_rag_qa_chain(gemini_model, vector_index)

        result = qa_chain.invoke({"query": question})

        return result
