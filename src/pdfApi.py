import warnings
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv()

# Classe responsável por conter e executar toda a lógica do QA-RAG implementado
class PdfApi:
	def __init__(self, pdfName="ppcbcc.pdf"):
		# Desativa os warnings da aplicação
		warnings.filterwarnings("ignore")
		
		# Caminho do PDF
		self.pdfPathName = "./pdfs/"+pdfName
		
		# API do Google AI Studio
		# Link para geração da API Key: https://aistudio.google.com/
		# A mesma deve estar no arquivo .env e carregada com o código abaixo:
		self.GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')
		
		# Modelo Gemini
		self.GEMINI_MODEL_NAME = "gemini-pro"
		
		# Nome do Embedding usado
		self.EMBEDDING_MODEL_NAME = "models/embedding-001"
		
		# A temperatura permite controlar o equilíbrio entre precisão e criatividade na geração de texto. 
		# Um valor mais baixo fornece saídas mais conservadoras e factuais;
		# Já um valor mais alto retorna maior aleatoriedade, gerando textos mais criativos e inesperados.
		self.TEMPERATURE = 0.5975
		
		# Define o tamanho das seções do PDF que serão processadas pelo aplicativo. 
		#  Um valor de 20.000 significa que o PDF será dividido em blocos de 20.000 
		#  palavras (ou caracteres) para facilitar o processamento. Essa divisão em 
		#  "pedaços" pode otimizar o uso da memória e o desempenho geral do aplicativo, 
		#  especialmente ao lidar com documentos extensos.
		# Escolheu-se esse valor de 20000 após diversos testes onde, devido o tamanho do
		#  arquivo e extensão de algumas informações, este foi o tamanho que conseguiu 
		#  apresentar resultados mais satisfatórios (não perfeitos) em relação a coesão.
		self.CHUNK_SIZE = 20000
		
		# Define a quantidade de texto que se repete entre seções consecutivas do PDF
		#  durante o processamento. Um valor de 2000 significa que cada chunk terá 2000
		#  palavras (ou caracteres) em comum com o chunk anterior. Essa sobreposição ajuda
		#  a manter o contexto do documento durante a análise, evitando que informações
		#  importantes sejam perdidas no processo de divisão em seções.
		# Escolheu-se esse valor pois corresponde a 10% do CHUNK_SIZE.
		# Nos testes, ao variar este valor, os demais resultados não foram satisfatórios.
		self.CHUNK_OVERLAP = 2000
		
		# Define o modelo de pergunta que será enviado ao modelo, ajuda a orientar a resposta do modelo 
		#  para que a mesma seja adequada para o contexto em questão.
		self.TEMPLATE = """Use os fragmentos de contexto a seguir para responder a questão no final. Deixe a resposta o mais concisa possível. Sempre diga "obrigado por perguntar!" no final da resposta. 
		{context}
		Question: {question}
		Helpful Answer:"""

	# Este método recebe um caminho para um arquivo PDF e retorna uma lista contendo todas as páginas do documento.
	def load_and_split_pdf(self, pdf_path):
		pdf_loader = PyPDFLoader(pdf_path)
		return pdf_loader.load_and_split()

	# Este método é responsável por configurar um modelo Gemini/Google utilizado para geração de texto. 
	# Seus parâmetros de entrada incluem o nome do modelo, a chave de API do Google AI Studio 
	#  e a configuração de temperatura.
	# Ao ser executada, ela retorna um modelo Gemini configurado, fazendo uso da classe 
	#  ChatGoogleGenerativeAI da biblioteca langchain_google_genai.
	def setup_gemini_model(self, model_name, api_key, temperature):
		return ChatGoogleGenerativeAI(
			model=model_name,
			google_api_key=api_key,
			temperature=temperature,
			convert_system_message_to_human=True,
		)

	# Essa função tem a finalidade de gerar embeddings para textos e estabelecer um índice 
	#  vetorial para recuperação desses textos. 
	# Seus parâmetros de entrada consistem em uma lista de textos, o nome do modelo 
	#  de embeddings e a chave da API. 
	# Ao ser executada, retorna um índice vetorial para recuperação de texto, utilizando
	#  a classe Chroma da biblioteca chroma.
	def create_embeddings_and_index(self, texts, model_name, api_key):
		embeddings = GoogleGenerativeAIEmbeddings(
				model=model_name, google_api_key=api_key
		)
		vector_index = Chroma.from_texts(texts, embeddings).as_retriever(
				search_kwargs={"k": 5}
		)
		return vector_index

	# Esse método tem como objetivo desenvolver uma cadeia de perguntas e respostas 
	#  (QA) usando a abordagem de geração aumentada por recuperação (RAG). 
	# Para sua execução, requer como entrada um modelo Gemini configurado e um índice
	#  vetorial para recuperação. 
	# O retorno consiste em uma cadeia RAG QA configurada, utilizando a classe 
	#  RetrievalQA da biblioteca langchain.chains.
	def create_rag_qa_chain(self, model, vector_index):
		QA_CHAIN_PROMPT = PromptTemplate.from_template(self.TEMPLATE)
		return RetrievalQA.from_chain_type(
			model, retriever=vector_index, return_source_documents=True,
			chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
		)

	# Este é o método responsável por executar o pipeline proposto pela aplicação.
	# Logo, é o método que é chamado pela API para gerar a resposta da pergunta requisitada.
	def pdf_response(self, question: str) -> str:
		# A partir do caminho do PDF, retorna as suas páginas devidamente separadas em uma única estrutura de dados
		pages = self.load_and_split_pdf(self.pdfPathName)
		
		# Instancia um separador de texto recursivo que recebe como parâmetro o CHUNK_SIZE e o CHUNK_OVERLAP.
		# Estes parâmetros ditam como o separador vai atuar sobre o texto fornecido.
		text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.CHUNK_SIZE, chunk_overlap=self.CHUNK_OVERLAP)
		
		# Agrupa todo o conteúdo das páginas do PDF em uma única string
		context = "\n\n".join(str(p.page_content) for p in pages)

		# Aplica o separador de texto na string com o conteúdo de todo o PDF
		texts = text_splitter.split_text(context)

		# Instancia o modelo Gemini com as suas configurações
		gemini_model = self.setup_gemini_model(self.GEMINI_MODEL_NAME, self.GOOGLE_API_KEY, self.TEMPERATURE)
		
		# Cria o vetor de índices a partir do embedding escolhido e do conteúdo do PDF já separado
		vector_index = self.create_embeddings_and_index(texts, self.EMBEDDING_MODEL_NAME, self.GOOGLE_API_KEY)

		# Cria a cadeia QA-RAG a partir do modelo e do vetor de índices
		qa_chain = self.create_rag_qa_chain(gemini_model, vector_index)

		# Executa a cadeia e obtém a resposta
		result = qa_chain.invoke({"query": question})

		# Retorna a resposta
		return result
