import os

from celery import Celery

UPSTASH_REDIS_URL = os.getenv('UPSTASH_REDIS_URL', 'redis://:AcHYAAIjcDFmZjIxOTE3YmVhMmI0NDlkYTg3YjJjNGUyMTEyMzNmMnAxMA@deciding-scorpion-49624.upstash.io:6379/0')

app = Celery('fastapi_project', broker=UPSTASH_REDIS_URL, backend=UPSTASH_REDIS_URL)

# Настройки по умолчанию
app.conf.update(
    accept_content=['json'],
    task_serializer='json',
    result_serializer='json',
    timezone='UTC'
)
# для запуска celery используем celery -A celery_config.app worker -l info -P eventlet