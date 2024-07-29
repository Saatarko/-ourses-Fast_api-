import os

from celery import Celery

# REDIS и CELERY настройки
UPSTASH_REDIS_URL = os.getenv('UPSTASH_REDIS_URL', 'https://deciding-scorpion-49624.upstash.io')
UPSTASH_REDIS_TOKEN = os.getenv('UPSTASH_REDIS_TOKEN', 'AcHYAAIjcDFmZjIxOTE3YmVhMmI0NDlkYTg3YjJjNGUyMTEyMzNmMnAxMA')

CELERY_BROKER_URL = f'redis://:{UPSTASH_REDIS_TOKEN}@{UPSTASH_REDIS_URL}/0'
CELERY_RESULT_BACKEND = f'redis://:{UPSTASH_REDIS_TOKEN}@{UPSTASH_REDIS_URL}/0'

app = Celery('fastapi_project', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

# Настройки по умолчанию
app.conf.update(
    accept_content=['json'],
    task_serializer='json',
    result_serializer='json',
    timezone='UTC'
)

# для запуска celery используем celery -A celery_config.app worker -l info -P eventlet