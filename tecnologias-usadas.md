# Tecnologias Usadas

Segue abaixo as tecnologias usadas para desenvolver o projeto, bem como uma breve descrição sobre elas e como elas foram utilizadas durante o desenvolvimento:

### Python

Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. É conhecida por sua sintaxe simples e legível, tornando-a ideal para iniciantes em programação.

> Link: https://www.python.org/

#### Funcionalidades

- **Tipagem dinâmica:** O tipo de uma variável não precisa ser declarado explicitamente, tornando o código mais conciso e fácil de escrever.
- **Orientação a objetos:** Suporta classes, objetos, herança e polimorfismo, permitindo a criação de código modular e reutilizável.
- **Interpretada:** O código Python é interpretado linha por linha, dispensando a necessidade de compilação, tornando o desenvolvimento mais rápido e interativo.
- **Ampla biblioteca padrão:** Possui uma biblioteca padrão extensa com diversas funções para tarefas comuns, como manipulação de strings, acesso a arquivos e redes, e muito mais.
- **Grande comunidade:** Possui uma comunidade grande e ativa que oferece suporte e ajuda aos desenvolvedores.

#### Função no código

- Foi a linguagem escolhida para construir toda a aplicação, tendo em vista a sua ótima compatibilidade com o restante das tecnologias adotadas.

### Langchain (framework)

Langchain é um framework de código aberto para construir e implantar aplicativos com modelos de linguagem, especialmente modelos de linguagem grande (LLMs) como Bard, GPT-3 e LaMDA.

> Link: https://www.langchain.com/

#### Funcionalidades

- **Abstrações básicas e linguagem de expressão:** Langchain oferece abstrações básicas para construir pipelines de processamento de linguagem natural (PLN) e uma linguagem de expressão para definir facilmente o fluxo de dados entre os componentes.
- **Componentes modulares:** O framework fornece uma variedade de componentes modulares para tarefas como pré-processamento de texto, geração de embeddings, recuperação de informações, tradução, resposta a perguntas e geração de texto.
- **Arquiteturas pré-construídas:** Langchain inclui arquiteturas pré-construídas para casos de uso comuns, como chatbots, sistemas de perguntas e respostas e ferramentas de resumo de texto.
- **Integrações:** O framework se integra com diversas ferramentas e bibliotecas populares de PLN, como Hugging Face Transformers, spaCy e TensorFlow.

#### Função no código

- Através do classe `PyPDFLoader` do pacote `langchain_community.document_loaders`, faz o carregamento do documento PDF;
- Através do método `load_and_split()` da classe`PyPDFLoader`, faz a separação do documento PDF carregado;
- Por meio do método `RecursiveCharacterTextSplitter`, cria um _text splitter_ que efetua a separação do texto gerado a partir das páginas carregadas do documento PDF;
- Através da classe `PrompTemplate` e do método `from_template()`, prepara um modelo de pergunta para o _Chatbot_;
- Fazendo o uso da classe `RetrievalQA` e do método `from_chain_type()`, cria uma corrente de recuperação para _question answering_ (QA);
- Através da classe `Chroma` e do método `from_texts()` cria um vetor de alta performace a partir dos textos separados e de um embedding.

### Langchain-google-genai (biblioteca)

Estende o Langchain para ser integrado com os serviços do Google Generative AI.
Permite acesso a modelos como Gemini para geração de texto e criação de embeddings.

> Link: https://python.langchain.com/docs/integrations/llms/google_ai/

#### Funcionalidades

- **Acesso a modelos GenAI:** A biblioteca permite interagir com diversos modelos GenAI, como Gemini e Bard, através de uma interface simples e unificada.
- **Geração de texto:** Utilize os modelos GenAI para gerar textos de diferentes tipos, como resumos, respostas a perguntas, scripts, poemas, etc.
- **Criação de embeddings:** Crie embeddings de texto de alta qualidade usando os modelos GenAI, que podem ser utilizados em diversas tarefas de PLN, como classificação de texto, similaridade de documentos e clustering.
- **Fácil integração:** A biblioteca se integra facilmente com os pipelines de Langchain, permitindo que os desenvolvedores utilizem os modelos GenAI em conjunto com outras ferramentas de PLN.

#### Função no código

- A classe `ChatGoogleGenerativeAI` é responsável por configurar e fornecer métodos que interagem com modelo Gemini;
- O `GoogleGenerativeAIEmbeddings` é capaz de criar embeddings de texto da Google;

### PyPDF (biblioteca que dá suporte ao Langchain)

Biblioteca Python para trabalhar com documentos PDF.

> Link: https://github.com/py-pdf/pypdf

#### Funcionalidades

- Permite abrir, ler, manipular e escrever arquivos PDF;
- Realiza extração de texto, metadados e outras informações de PDFs.

### Função no código

- É usado para carregar e dividir o documento PDF em páginas.

### ChromaDB (biblioteca que dá suporte ao Langchain)

Banco de dados de vetores de alto desempenho para armazenar e recuperar dados com base na similaridade.

> Link: https://www.trychroma.com/

#### Funcionalidades

- Armazenamento e recuperação eficientes de vetores de alta dimensionalidade;
- Permite operações de busca rápida com base na similaridade de vetores.

#### Função no código

A classe Chroma do Langchain utiliza o ChromaDB para criar o vetor de armazenamento para recuperação de texto.

### Flask (microframework)

> Link: https://flask.palletsprojects.com/en/3.0.x/
> Flask é um microframework Python para desenvolvimento web. É conhecido por sua simplicidade, flexibilidade e modularidade, tornando-o ideal para criar aplicações web pequenas e escaláveis.

#### Funcionalidades

- **Rotas e visualizações:** Crie rotas para URLs e defina visualizações para gerar respostas HTTP dinâmicas;
- **Templates:** Utilize templates Jinja2 para integrar código Python com HTML e gerar páginas web dinâmicas;
- **Suporte a WSGI:** Implementação completa do WSGI, permitindo que o Flask seja executado em diversos servidores web;
- **Depuração integrada:** Ferramenta de depuração integrada para facilitar a identificação e correção de erros;
- **Extensões:** Ampla variedade de extensões disponíveis para adicionar funcionalidades ao Flask, como autenticação, gerenciamento de banco de dados e upload de arquivos.

#### Função no código

- Foi usado para criar uma API e expor um endpoint que, dado uma pergunta relacionada com o documento, retorna a resposta utilizando o _pipeline_ construído com os métodos e bibliotecas descritos anteriormente.

# Sobre as bibliotecas instaladas

Segue abaixo o trecho de código responsável por instalar as bibliotecas e frameworks supracitados no ambiente de desenvolvimento em Python:

```
pip install Flask
pip install langchain-community
pip install langchain-google-genai
pip install pyPDF
pip install chromadb
```
