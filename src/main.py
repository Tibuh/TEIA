from flask import Flask, request, jsonify
from pdfApi import PdfApi
from documentsApi import DocumentsApi
from flask_cors import CORS

# Este arquivo main.py é responsável por criar a API da aplicação com o Flask

app = Flask(__name__)
CORS(app)

#Rota padrão da API
@app.route("/")
def hello_world():
	return "<p>"+"API no ar!"+"</p>"

#Rota para requisitar, a partir de uma pergunta, uma resposta baseada no PDF
@app.post("/question")
def question_post():
	# Obtém o body da requisição
	data = request.json

	# Instancia a API de QA-RAG
	api = PdfApi()

	# Executa o pipeline de QA-RAG passando a pergunta que veio no body como parâmetro
	response = api.pdf_response(data.get('question'))

	# Retorna a resposta 
	return jsonify(
		response = response["result"],
	)

# Endpoint para listar os PDFs que estão armazenados no backend
# OBS.: este endpoint foi criado pensando em uma futura melhoria da aplicação
@app.get("/documents")
def documents_availables():
	# Lista os documentos presentes no backend
	listDocuments = DocumentsApi.Documents_avaibles()

	# Retorna os documentos
	return jsonify(
			documents = listDocuments
	)

if __name__ == '__main__':
	app.run(debug=False, port=5000, host='0.0.0.0')
