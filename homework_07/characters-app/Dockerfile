FROM python:3.13-bookworm

# Отключение кеширования
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY .env .

# Установка poetry
RUN python -m pip install --upgrade pip poetry && poetry config virtualenvs.create false
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main

COPY characters-app .

EXPOSE 8000



