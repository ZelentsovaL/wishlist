# Используем официальный образ Python
FROM python:3.12.7-slim-bullseye AS prod

# Устанавливаем необходимые зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Poetry через pip
RUN pip install poetry==1.8.2

# Создаем директории для проекта
WORKDIR /app/wishlist

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock /app/wishlist/

# Настраиваем Poetry
RUN poetry config virtualenvs.create false

# Устанавливаем зависимости
RUN poetry install --only main

# Очищаем кэш
RUN apt-get purge -y && rm -rf /var/lib/apt/lists/*

# Копируем приложение
COPY . /app/wishlist/