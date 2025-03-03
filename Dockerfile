ARG WORKDIR="/app"

# --- Builder image ---

FROM python:3.12-alpine AS builder

ARG WORKDIR

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR ${WORKDIR}

RUN pip install poetry \
    && poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./

RUN poetry install

# --- Target image ---

FROM python:3.12-alpine

ARG WORKDIR

WORKDIR ${WORKDIR}

COPY --from=builder ${WORKDIR} .

COPY ./src/ ./src

ENV PYTHONPATH "${PYTHONPATH}:/app/src"
ENV PATH "/app/.venv/bin:$PATH"

EXPOSE 8000
CMD uvicorn main:create_app --host 0.0.0.0 --factory
