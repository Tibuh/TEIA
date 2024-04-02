from flask import Flask, request, jsonify
from pdfApi import PdfApi
from documentsApi import DocumentsApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>"+"Ta rodando pae"+"</p>"

@app.post("/question")
def question_post():
    data = request.json

    pathName = data.get('document')    
    api = PdfApi(pathName)

    response = api.pdf_response(data.get('question'))

    return jsonify(
        response = response["result"],
    )
@app.get("/documents")
def documents_availables():
    listDocuments = DocumentsApi.Documents_avaibles()

    return jsonify(
        documents = listDocuments
    )

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
