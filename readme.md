# Projeto AI Gemini

Este é um projeto de demonstração utilizando a API do Google Generative AI & streamlit.

1º Objetivo é criar uma aplicação web para que o usuário possa fazer perguntas em linguagem natural.

2º Objetivo utiliizar a API do Google Generative AI para criar uma query SQLite seguindo a modelagem do banco de dados e que responda a pergunta do usuário.

3º Objetivo é executar a consulta internamente de forma isolada e retornar a resposta para a pergunta do usário também em linguagem natural.

## Requisitos
    Python 3.9 ou superior
    Adicione sua Google API KEY no arquivo .env

## Instalação

Para iniciar recomendo utilizar a criação de um ambiente virutal executando o comando python abaixo no terminal:

```python.exe -m venv .venv```

Para acessar o ambiente virtual criado utilize o comando abaixo:

```.venv/Scripts/activate```

Uma boa recomendação é atualizar o pip para a versão mais recente.

```python.exe -m pip install --upgrade pip --no-cache-dir```

Para instalar as dependências do projeto utilize o comando abaixo:

```pip install -q -U -r google.generativeai```

```pip install streamlit```

Para iniciar o projeto utilize o comando abaixo:

```streamlit run app.py```

## Como Usar

Acesse no navegador o localhost no link: http://localhost:8501

Basta escrever uma pergunta sobre as informações que precisar sobre fornecedores, clientes, produtos e vendas.

![exemplo_contatos](https://raw.githubusercontent.com/Bruno-Henrique-Almeida/gemini_streamlit/main/img/exemplo_contatos_cliente_fornecedor.png)

![exemplo_melhor_cliente](https://raw.githubusercontent.com/Bruno-Henrique-Almeida/gemini_streamlit/main/img/exemplo_melhor_cliente.png)

![exemplo_melhor_produto_anual](https://raw.githubusercontent.com/Bruno-Henrique-Almeida/gemini_streamlit/main/img/exemplo_melhor_produto_anual.png)

![exemplo_pior_produto](https://raw.githubusercontent.com/Bruno-Henrique-Almeida/gemini_streamlit/main/img/exemplo_pior_produto.png)