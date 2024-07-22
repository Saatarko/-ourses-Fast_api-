# Используем официальный Python образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями
COPY pyproject.toml poetry.lock /app/

# Устанавливаем Poetry и зависимости
RUN pip install poetry
RUN poetry install --no-root

# Копируем весь код проекта
COPY . /app/

# Устанавливаем переменную окружения для FastAPI
ENV PYTHONPATH=/app

# Команда для запуска приложения
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "127.0.0.0", "--port", "8000"]