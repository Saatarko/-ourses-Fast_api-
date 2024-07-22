
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr

from core.celery.config import app

# Конфигурация для отправки email
conf = ConnectionConfig(
    MAIL_USERNAME='MS_5s0tFc@trial-3zxk54vy91z4jy6v.mlsender.net',
    MAIL_PASSWORD='ll4Kv7aUY2tgb2VB',
    MAIL_FROM='MS_5s0tFc@trial-3zxk54vy91z4jy6v.mlsender.net',
    MAIL_PORT=587,
    MAIL_SERVER='smtp.mailersend.net',
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False
)


@app.task
async def send_email_task(subject: str, recipient: EmailStr, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[recipient],
        body=body,
        subtype="plain"
    )

    fm = FastMail(conf)

    await fm.send_message(message)

# для запуска celery используем celery -A celery_config.app worker -l info -P eventlet