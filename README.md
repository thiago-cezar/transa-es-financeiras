## Resumo da Configuração do Projeto

### 1. Clone o repositório do GitHub, usando o seguinte comando:

- `git clone git@github.com:thiago-cezar/transacoes-financeiras.git`

### 2 Instale as dependências, usando o seguinte comando:

- e recomendável que você instale as dependências do projeto em um ambiente virtual, voce poder fazer isso utilizando os comandos.
- `python -m venv myenv`

### Windows

myenv\Scripts\activate.bat

### Linux/macOS

source myenv/bin/activate

- Apos ativar o ambiente virtual instale as dependências
- `pip install -r requirements.txt`

### 3. Instale o PostgreSQL em seu sistema operacional.

- [Link para a instalação](https://www.postgresql.org/download/)
- Crie um banco de dados no PostgreSQL usando o console de comando.

### 4. Configure as Variáveis de Ambiente

- faça uma copia do arquivo .env na raiz do projeto e configure as seguintes variáveis de ambiente:

- `SECRET_KEY=<sua-chave-secreta>`
- `POSTGRES_USERNAME=<nome-de-usuario-do-banco>`
- `POSTGRES_PASSWORD=<senha-do-banco>`
- `POSTGRES_DB_NAME=<nome-do-banco>`

### 5. Execute as migrations, usando os seguintes comandos:

- `python manage.py makemigrations`
- `python manage.py migrate`

### 6. Inicie o servidor de desenvolvimento, usando o seguinte comando:

- `python manage.py runserver`
- Agora, você pode acessar a API em [http://localhost:8000/api/](http://localhost:8000/api/).

# API CNAB movimentações financeiras

## Introdução

Esta API foi desenvolvida com o objetivo de fornecer uma interface para a interação com um banco de dados relacional e para envio de arquivos.

Para isso, utilizamos o DjangoRestFramework como framework principal e o Python-dotenv para lidar com as variáveis de ambiente.

## Rotas

- api/balance/: Rota que retorna a soma dos valores do saldo.
- api/send/: Rota que recebe o arquivo .txt com os dados CNAB e os envia para as tabelas.

## Requisições

- GET: api/balance/ - Retorna a soma dos valores do saldo.
- POST: api/send/ - Envia o arquivo .txt com os dados CNAB para as tabelas.

## Respostas

- A resposta da API será no formato JSON.

  Exemplo de resposta para a rota api/balance/:

  `{
"id": 1,
"saldo": -102.0,
"Nome_loja": "BAR DO JOÃO"
}`

## Conclusão

Esta API fornece uma interface simples e intuitiva para a interação com um banco de dados relacional e para envio de arquivos .txt com códigos cnab que serão lidos e armazenados, facilitando a integração com outras aplicações.

Além disso, a utilização de tecnologias como DjangoRestFramework e Python-dotenv garante uma aplicação segura e escalável.
