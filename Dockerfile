FROM python:3.13-slim

WORKDIR /tax_app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

COPY tax_app ./tax_app
COPY . .

EXPOSE 8000
CMD ["poetry", "run", "prod"]