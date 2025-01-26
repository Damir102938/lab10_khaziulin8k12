# Multi-stage build

# Stage 1: Build the app
FROM python:3.9-slim as builder

# Устанавливаем необходимые пакеты для компиляции psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Run the app
FROM python:3.9-slim

WORKDIR /app

# Копируем все из первого этапа (в том числе установленные пакеты)
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY . /app/

# Применяем collectstatic в данном контейнере
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "my_microservice.wsgi:application", "--bind", "0.0.0.0:8000"]
