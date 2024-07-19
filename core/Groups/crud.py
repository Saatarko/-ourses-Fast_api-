import asyncio
from datetime import datetime
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from core.Groups.schemas import GroupsSchemasCreate, GroupsSchemasTakeOne
from core.models import User, Groups
from sqlalchemy.engine import Result
from api.api_v1.fastapi_user_routers import current_user
from core.schemas.user import UserRead


async def create_groups(
    session: AsyncSession,
    groupe_in: GroupsSchemasCreate,
    user: User
) -> Groups:
    # Проверка, залогинен ли пользователь
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    # Получаем текущее время
    date_start = datetime.now()

    # Убедитесь, что courses_id - это не кортеж
    courses_id = groupe_in.courses_id  # Исправление: убран лишний запятая

    # Создаем объект группы
    groups = Groups(
        name=groupe_in.name,
        courses_id=courses_id,
        date_start=date_start  # Используйте date_start как объект datetime
    )

    # Добавление группы в сессию и коммит
    session.add(groups)
    await session.commit()
    await session.refresh(groups)  # Обновляем объект группы для получения id и других значений из БД

    return groups


async def get_groups(session: AsyncSession, user: User) -> list[Groups]:  # ожидаем список групп

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    stmt = select(Groups).order_by(Groups.id)  # получаем списолк и
    result: Result = await session.execute(stmt)  # получаем резуллттат
    groups = result.scalars().all()
    return list(groups)


async def get_one_group(session: AsyncSession, groupe_in: GroupsSchemasTakeOne, user: User) -> Groups:  # ожидаем данные по 1 челвеку

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    name = groupe_in.name

    stmt = select(Groups).filter(Groups.name == name).order_by(Groups.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    groupe = result.scalars().first()
    return groupe