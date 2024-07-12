import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from core.Status.schemas import StatusSchemasCreate
from core.models import Status
from sqlalchemy.engine import Result


async def create_status(
    session: AsyncSession, status_in: StatusSchemasCreate
) -> Status:
    status = Status(**status_in.model_dump())
    session.add(status)
    await session.commit()
    await session.refresh(
        status
    )  # обновляем данные перед возвратом ибо двигло асинхронное малоли шо
    return status


async def get_status(session: AsyncSession) -> list[Status]:  # ожидаем список курсов
    stmt = select(Status).order_by(Status.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    status = result.scalars().all()
    return list(status)
