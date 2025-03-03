FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./app/ ./

ENV PYTHONPATH "${PYTHONPATH}:/app"

EXPOSE 8000
CMD uvicorn main:create_app --host 0.0.0.0 --factory
