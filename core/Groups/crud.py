import asyncio
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from core.Groups.schemas import GroupsSchemasCreate
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

    date = func.now()
    date_start = date.strftime('%Y-%m-%d %H:%M:%S')

    courses_id = groupe_in.courses_id,

    groups = Groups(
        name=groupe_in.name,
        courses_id=courses_id,
        date_start=date_start
    )

    session.add(groups)
    await session.commit()
    await session.refresh(groups)  # обновляем данные перед возвратом
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
