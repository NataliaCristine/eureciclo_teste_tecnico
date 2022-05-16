# Introdução

Uma aplicação web que faz o upload de arquivos txt, separados por tab, salva em banco de dados não relacional e exibe para o usuário.

# Ambiente

## Dependências

- Ambiente Linux ou Windows (WSL2) + docker
- Python 3.8+ (instalado no Linux ou WSL2)

## Construindo o Ambiente

Antes de executar as instalações é importante ter o linux atualizado. Podendo utilizar o comando abaixo:

> sudo apt update && upgrade

Depois instale o python:

> sudo apt install python3 python3-pip\

Depois instale o Docker e docker-compose:
Instale o docker conforme documentação do site oficial:
[Instalação do docker via repositório](http://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

# Executar o Projeto

### Esse passo é baixar o projeto

https://github.com/NataliaCristine/eureciclo_teste_tecnico.git

Se tiver ssh configurada utilize:
git@github.com:NataliaCristine/eureciclo_teste_tecnico.git

## Rodar o Projeto

Para rodar o projeto deve utilizar o comando:

> docker-compose up

### Utilização

Para utilizar deve acessar o navegador, como por exemplo google chorme e digitar a rota.

## Rotas e exemplo de uso

### Upload do arquivo

> http://localhost:5000

- Nesta rota será enviado um arquivo.txt para fazer isso clique em escolher arquivo. Em seguida vai abrir uma janela selecione o arquivo clique em abrir. Depois é só clicar em submit. Em seguida vc será redirecionado para página http://localhost:5000/register que irá exibir uma tabela com as informações e a receita total.

- Caso não envie um arquivo ou seja de outro formato aparecerá na página a informação de erro e um botão de voltar que irá te direcionar para o upload.

- Caso queira ver os registros da tabela clique no botão tabela registros

- Caso esteja na rota http://localhost:5000/register e queira voltar para upload basta clicar em eureciclo.

## Executando os testes

### Rodar o testes

- Para isso você deve criar um ambiente virtual com o comando:

  > python3 -m venv venv

- Entrar no ambiente virtual com o comando:

  > source venv/bin/activate

- Instalar as dependências com o comando:

  > pip install -r requirements.txt

- Depois rodar o comando:
  > pytest -svv
