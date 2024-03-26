from flask import Flask, request, jsonify
from pdfApi import PdfApi

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>"+"Ta rodando pae"+"</p>"

@app.post("/question")
def question_post():
    data = request.json

    api = PdfApi()

    response = api.pdf_response(data.get('question'))

    return jsonify(
        response = response["result"],
    )

if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')