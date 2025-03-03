FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-ansi

COPY ./src/ ./src

ENV PYTHONPATH "${PYTHONPATH}:/app/src"
ENV PATH "/app/.venv/bin:$PATH"

EXPOSE 8000
CMD uvicorn main:create_app --host 0.0.0.0 --factory
