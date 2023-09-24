FROM python:3.8-slim

ENV POETRY_VERSION=1.1.12

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app/
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false \
  && poetry install

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]