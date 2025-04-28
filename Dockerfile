FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY /app ./app

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000
CMD ["poetry", "run", "prod"]