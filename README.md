# Pokédex API

A **Pokédex API** é um projeto desenvolvido como trabalho de conclusão do curso de **Back-end com Python da EBAC**.

O projeto tem como objetivo consolidar e demonstrar os conhecimentos adquiridos ao longo do curso, além de compor meu portfólio profissional na área de desenvolvimento Back-end.

A API permite gerenciar uma Pokédex por meio de operações de criação, listagem, consulta por ID ou nome, atualização e exclusão de Pokémon, oferecendo uma estrutura para o armazenamento e gerenciamento dessas informações.

## Tecnologias utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Python 3.14:** linguagem de programação utilizada no desenvolvimento da aplicação.
- **FastAPI:** framework utilizado para a construção da API REST.
- **Uvicorn:** servidor ASGI responsável por executar a aplicação.
- **SQLAlchemy:** biblioteca utilizada para o mapeamento objeto-relacional (ORM) e interação com o banco de dados.
- **PostgreSQL 17:** sistema gerenciador de banco de dados utilizado para armazenar as informações dos Pokémon.
- **Pydantic:** biblioteca utilizada para validação e estruturação dos dados.
- **Poetry:** ferramenta utilizada para gerenciamento de dependências e ambiente do projeto.
- **Docker:** ferramenta utilizada para criar e executar containers.
- **Docker Compose:** utilizado para orquestrar os serviços da aplicação e do banco de dados.
- **Pytest:** framework utilizado para execução dos testes automatizados.

## Funcionalidades

A Pokédex API disponibiliza as seguintes operações:

- Cadastrar novos Pokémon na Pokédex.
- Listar os Pokémon cadastrados.
- Buscar Pokémon pelo ID.
- Buscar Pokémon pelo nome.
- Atualizar informações de Pokémon cadastrados.
- Excluir Pokémon da Pokédex.
- Verificar o status de funcionamento da API.

## Instalação e configuração

### Pré-requisitos

Para executar o projeto utilizando Docker, é necessário ter instalado:

- Docker.
- Docker Compose.
- Git.

Para executar os testes localmente, também é necessário ter:

- Python 3.14.
- Poetry.

### Clonando o repositório

Clone o repositório utilizando o comando:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd Projeto_Final_Python
```

### Configurando as variáveis de ambiente

Na raiz do projeto, crie um arquivo `.env` utilizando o `.env.example` como referência.

Preencha as variáveis necessárias para estabelecer a conexão com o banco de dados PostgreSQL.

**Importante:** não compartilhe o arquivo `.env`, pois ele contém informações de configuração que não devem ser expostas publicamente.

## Execução com Docker

Com as variáveis de ambiente configuradas, execute os seguintes comandos na raiz do projeto.

### Iniciando os containers

Para construir a imagem da aplicação e iniciar os serviços, utilize:

```bash
docker compose up -d --build
```

### Verificando os containers

Para verificar se os serviços da API e do banco de dados estão em execução, utilize:

```bash
docker compose ps
```

### Acessando a documentação da API

Após iniciar os containers, a documentação interativa da API estará disponível em:

http://localhost:8000/docs

Também é possível verificar o status da aplicação pelo endereço:

http://localhost:8000/health

### Encerrando os containers

Para interromper os serviços, execute:

```bash
docker compose down
```

## Estrutura do projeto

O projeto está organizado da seguinte forma:

```text
Projeto_Final_Python/
│
├── app/
│   ├── routers/
│   │   └── pokemon.py
│   │
│   ├── services/
│   │   └── pokemon_service.py
│   │
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── pokeapi.py
│   ├── schemas.py
│   └── __init__.py
│
├── tests/
│   ├── conftest.py
│   └── test_pokemon.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
└── README.md
```

### Descrição dos diretórios e arquivos

- **app/:** contém o código principal da aplicação.
- **app/routers/:** reúne as rotas e os endpoints relacionados aos Pokémon.
- **app/services/:** contém a lógica de serviços utilizada pela aplicação.
- **database.py:** configura a conexão com o banco de dados.
- **main.py:** inicializa a aplicação FastAPI.
- **models.py:** define os modelos utilizados na interação com o banco de dados.
- **pokeapi.py:** reúne funcionalidades relacionadas à integração com a PokéAPI.
- **schemas.py:** define os esquemas e a validação dos dados.
- **tests/:** contém os testes automatizados da aplicação.
- **conftest.py:** reúne configurações e recursos compartilhados pelos testes.
- **test_pokemon.py:** contém os testes relacionados às funcionalidades dos Pokémon.
- **Dockerfile:** define a construção da imagem da aplicação.
- **docker-compose.yml:** configura e orquestra os containers da aplicação e do banco de dados.
- **pyproject.toml:** contém as configurações e dependências do projeto.
- **poetry.lock:** registra as versões específicas das dependências instaladas.
- **.env.example:** disponibiliza um modelo das variáveis de ambiente necessárias.
- **.gitignore:** define arquivos e diretórios que não devem ser enviados ao Git.
- **.dockerignore:** define arquivos e diretórios que devem ser ignorados durante a construção da imagem Docker.

## Endpoints da API

A API disponibiliza os seguintes endpoints para gerenciamento dos Pokémon:

| Método HTTP | Endpoint | Descrição |
|---|---|---|
| GET | `/` | Retorna uma mensagem de boas-vindas. |
| GET | `/health` | Verifica o status de funcionamento da API. |
| GET | `/pokemon` | Lista os Pokémon cadastrados. |
| POST | `/pokemon` | Cadastra um novo Pokémon. |
| GET | `/pokemon/id/{pokemon_id}` | Busca um Pokémon pelo ID. |
| GET | `/pokemon/{name}` | Busca um Pokémon pelo nome. |
| PUT | `/pokemon/{pokemon_id}` | Atualiza as informações de um Pokémon. |
| DELETE | `/pokemon/{pokemon_id}` | Exclui um Pokémon pelo ID. |

### Exemplo de cadastro de Pokémon

Para cadastrar um Pokémon, envie uma requisição `POST` para `/pokemon` com um corpo JSON como o exemplo abaixo:

```json
{
    "name": "Pikachu",
    "type": "Electric",
    "level": 25
}
```

## Executando os testes

O projeto utiliza o **Pytest** para executar testes automatizados e verificar o funcionamento das funcionalidades da API.

Para executar os testes localmente, certifique-se de que as dependências estejam instaladas e que as configurações necessárias para o ambiente de testes estejam disponíveis.

Na raiz do projeto, instale as dependências:

```bash
poetry install
```

Execute os testes:

```bash
poetry run pytest
```

Para visualizar um resumo mais detalhado da execução dos testes, utilize:

```bash
poetry run pytest -v
```

O Pytest executará os testes disponíveis no diretório `tests/` e exibirá os resultados no terminal.