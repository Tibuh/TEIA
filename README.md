# TEIA

Projeto direcionado para unidade 2

## Infos

Versão do python: 3.12.2

## Preparação do ambiente

Primeiro deve-se criar um ambiente virtual na pasta do projeto com o seguinte comando:

Linux:

```
python3 -m venv .venv
```

Windows:

```
py -3 -m venv .venv
```

Logo em seguida, deve-se ativar o ambiente virtual:

Linux:

```
. .venv/bin/activate
```

Windows:

```
.venv\Scripts\activate
```

> Obs: caso dê erro informando que não é possível executar scripts no powershell execute esse comando no powershell como administrador: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`

Após ativar o ambiente virtual, instale as dependências:

## Libs necessárias

```
pip install Flask
pip install --quiet langchain-community
pip install --quiet langchain-google-genai
pip install --quiet pyPDF
pip install --quiet chromadb
```
