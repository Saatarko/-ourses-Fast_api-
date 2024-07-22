import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from fastapi import Request
from pydantic import EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

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


async def send_email(subject: str, recipient: EmailStr, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[recipient],  # Список получателей
        body=body,
        subtype="plain"
    )

    # Создание экземпляра FastMail
    fm = FastMail(conf)

    # Отправка сообщения (эта функция должна быть вызвана асинхронно)
    await fm.send_message(message)
