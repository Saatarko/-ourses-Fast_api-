import asyncio
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.People.schemas import PeopleSchemasCreate, PeopleSchemasUpdate
from core.models import People, User
from sqlalchemy.engine import Result
from api.api_v1.fastapi_user_routers import current_user
from core.schemas.user import UserRead


async def create_people(
    session: AsyncSession,
    people_in: PeopleSchemasCreate,
    user: User
) -> People:
    # Проверка, залогинен ли пользователь
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    # Установите status_id в значение 1 по умолчанию
    status_id = 1

    # Получите user_id из текущего пользователя
    user_id = user.id

    # Создайте объект People с установленными user_id и status_id
    people = People(
        first_name=people_in.first_name,
        last_name=people_in.last_name,
        age=people_in.age,
        user_id=user_id,
        status_id=status_id
    )

    session.add(people)
    await session.commit()
    await session.refresh(people)  # обновляем данные перед возвратом
    return people



async def get_people(session: AsyncSession) -> list[People]:  # ожидаем список людей
    stmt = select(People).order_by(People.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    people = result.scalars().all()
    return list(people)

async def get_one_people(session: AsyncSession, pk: int, user: User) ->People:  # ожидаем данные по 1 челвеку

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    stmt = select(People).filter(People.id==pk).order_by(People.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    people = result.scalars().first()
    return people


async def update_one_people(session: AsyncSession,
                            pk: int,
                            people_in: PeopleSchemasUpdate,
                            user: User) -> People:
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    stmt = select(People).filter(People.id == pk).order_by(People.id)
    result: Result = await session.execute(stmt)
    people = result.scalars().first()

    if people is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="People not found",
        )

    people.first_name = people_in.first_name
    people.last_name = people_in.last_name
    people.age = people_in.age

    await session.commit()
    await session.refresh(people)
    return people

