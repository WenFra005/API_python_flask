# API_python_flask

## O que o código faz

Esta é uma API REST simples desenvolvida com **FastAPI** que gerencia dados de atletas. A aplicação permite:

- **Criar atletas**: Registrar novos atletas com nome, CPF, centro de treinamento e categoria
- **Listar atletas**: Recuperar a lista de atletas com paginação

## Características principais

- Banco de dados SQLite para persistência de dados
- Validação de dados com Pydantic
- Paginação automática na listagem
- Proteção contra CPFs duplicados

## Como executar

### 1. Instale as dependências

```bash
pip install fastapi uvicorn sqlalchemy pydantic fastapi-pagination
```

### 2. Navegue até o diretório do projeto

```bash
cd /home/wendell/Documentos/python/API_python_flask/src/main/workout_api
```

### 3. Execute a aplicação

```bash
uvicorn main:app --reload
```

### 4. Acesse a API

- **Documentação interativa**: http://localhost:8000/docs
- **Alternativa**: http://localhost:8000/redoc

## Endpoints disponíveis

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/atletas/` | Criar novo atleta |
| GET | `/atletas/` | Listar atletas com paginação |