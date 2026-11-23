FROM python:3.14-slim

# Evita buffer de logs e arquivos .pyc desnecessários
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
# Instala o Poetry
RUN pip install --no-cache-dir poetry
# Copia o restante do código da aplicação
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root --no-interaction --no-ansi
COPY . .

CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
