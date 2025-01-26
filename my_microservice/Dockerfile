# Multi-stage сборка

# Этап 1: Сборка
FROM python:3.9-slim as builder


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Этап 2: Запуск
FROM python:3.9-slim

WORKDIR /app


COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . /app/


RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "my_microservice.wsgi:application", "--bind", "0.0.0.0:8000"]
