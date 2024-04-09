- Gabriel de Oliveira Santos / g4briel720@academico.ufs.br / 0009-0002-5996-3365
- Gustavo Caetano Santos / gustavocaetano@academico.ufs.br / 0009-0005-1756-9556
- Vitor Hugo Ribeiro Tibutrino de Melo / vitor.hugo@academico.ufs.br / 0009-0003-3816-8933

# Secretar.ia

Projeto desenvolvido como parte da avaliação final na disciplina de Tópicos Especiais em Inteligência Artificial na Universidade Federal de Sergipe.

### Acesse a aplicação:
> **Obs.:** para testar a aplicação, é preciso informar com antecedência para que possamos ligar o ambiente da AWS e, consequentemente, subir o backend.
[Clique aqui para acessar a aplicação.](https://6614b252fd23f900081c496c--secretar-ia.netlify.app/)

### Tecnologias usadas:

[Clique aqui para acessar o relatório.](https://github.com/Tibuh/TEIA/blob/main/tecnologias-usadas.md)

### Artigo/Short Paper
[Clique aqui para acessar o documento.](https://github.com/Tibuh/TEIA/blob/main/Artigo%20-%20Secretar.ia.docx)

### Repositório do Front-End

[Clique aqui para acessá-lo.](https://github.com/Gustavo-caetano/TEIA-Frontend).


### Sobre o projeto

O projeto se trata de um estudo de caso referente ao desenvolvimento de aplicações que fazem uso de Inteligência Artificial. Mais especificamente, no contexto de _Retrieval Augmented Generation_ (RAG).
Resumindo, se trata de uma aplicação WEB que, por meio de um Chatbot, consegue responder perguntas relacionadas a um documento previamente escolhido que, neste caso, foi o **Projeto Pedagógico do Curso de Graduação em Ciência da Computação da Universidade Federal de Sergipe**. 
> O Projeto Pedagógico pode ser acessado [aqui](https://github.com/Tibuh/TEIA/blob/main/src/pdfs/ppcbcc.pdf).

Para isso, implementou-se um _pipeline_ de QA-RAG (_Question Answering_ RAG) utilizando a **API Gemini Pro** da Google com auxílio do _framework_ **LangChain** e algumas outras bibliotecas relacionadas a ele.

#### Diagrama do pipeline QA-RAG implementado na aplicação:
![diagrama pipeline](https://github.com/Tibuh/TEIA/assets/66384277/406b34b6-9e9f-482f-8669-aa9c676e9dd5)


O backend da aplicação (correspondente à este repositório) é feito em Python, com auxílio do framework Flask.

#### Diagrama de implantação da aplicação:
![Diagrama de Implantação 2](https://github.com/Tibuh/TEIA/assets/66384277/4d46e45d-1719-4e6c-951d-ab02308af528)

### Como executar o projeto:

#### Pré requisitos:

- API Key do Google AI Studio, para ter acesso ao modelo do Gemini-Pro e o Embedding-001;
  - Pode ser obtida por este [link](https://aistudio.google.com/).
- Docker;
- Docker-Compose;
- Algum cliente de API REST (Postman, Insomnia, etc.) para efetuar requisições.

#### Passo a passo

```
 git clone https://github.com/Tibuh/TEIA.git
 cd ./TEIA
 docker-compose up -d --build
```

Quando o Docker criar a imagem e subir o container da aplicação, a API poderá ser acessada a partir da url `http://localhost:3500/`.

Para efetuar uma pergunta, basta enviar uma requisição do tipo **POST** para o endpoint `http://localhost:3500/question`, com o seguinte _body_:

```
{
  "question": SUA_PERGUNTA
}
```

#### Exemplo de requisição utilizando o Postman
![image](https://github.com/Tibuh/TEIA/assets/66384277/ce7bc792-72ef-43d9-a92f-9f365c322838)

