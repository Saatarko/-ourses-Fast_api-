from celery import Celery

# REDIS и CELERY настройки
REDIS_HOST = '127.0.0.1'
REDIS_PORT = '6379'

CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'

app = Celery('fastapi_project', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

# Настройки по умолчанию
app.conf.update(
    accept_content=['json'],
    task_serializer='json',
    result_serializer='json',
    timezone='UTC'
)


# для запуска celery используем celery -A celery_config.app worker -l info -P eventlet