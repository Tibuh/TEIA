- Gabriel de Oliveira Santos / g4briel720@academico.ufs.br / 0009-0002-5996-3365
- Gustavo Caetano Santos / gustavocaetano@academico.ufs.br /
- Vitor Hugo Ribeiro Tibutrino de Melo / vitor.hugo@academico.ufs.br /

# Secretar.ia

Projeto desenvolvido como parte da avaliação final na disciplina de Tópicos Especiais em Inteligência Artificial na Universidade Federal de Sergipe.

### Tecnologias usadas:

[Clique aqui para acessar o relatório.](https://github.com/Tibuh/TEIA/blob/main/tecnologias-usadas.md)

### Repositório do Front-End

[Clique aqui para acessá-lo](https://github.com/Gustavo-caetano/TEIA-Frontend).

### Sobre o projeto

O projeto se trata de um estudo de caso referente ao desenvolvimento de aplicações que fazem uso de Inteligência Artificial. Mais especificamente, no contexto de _Retrieval Augmented Generation_ (RAG).

A aplicação consiste em um chatbot especializado em responder perguntas relacionadas ao Projeto
Pedagógico do Curso de Graduação
em Ciência da Computação da Universidade Federal de Sergipe.

> O Projeto Pedagógico pode ser acessado [aqui](https://github.com/Tibuh/TEIA/blob/main/src/pdfs/ppcbcc.pdf).

O backend da aplicação (correspondente à este repositório) é feito em Python, com auxílio do framework Flask.

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

