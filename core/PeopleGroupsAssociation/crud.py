import asyncio
from typing import Annotated, List

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from core.PeopleGroupsAssociation.schemas import PeopleGroupsAssociationSchemasCreate, OnePeopleGroupsSchemasResponse
from core.models import User, PeopleGroupsAssociation, People, Groups
from sqlalchemy.engine import Result
from api.api_v1.fastapi_user_routers import current_user
from core.schemas.user import UserRead


async def get_peoples_and_groups(session: AsyncSession) -> list[PeopleGroupsAssociation]:  # ожидаем список людей
    stmt = select(PeopleGroupsAssociation).order_by(PeopleGroupsAssociation.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    people_and_groups = result.scalars().all()
    return list(people_and_groups)


async def create_peoples_and_groups(

        session: AsyncSession,
        people_and_groups_in: PeopleGroupsAssociationSchemasCreate,
        user: User,

) -> PeopleGroupsAssociation:
    # Проверка, залогинен ли пользователь
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    # Получите user_id из текущего пользователя
    temp_id = user.id

    stmt = select(People).filter(People.user_id == temp_id).order_by(People.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    people = result.scalars().first()

    if people is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Профиль не заполнен. Заполните пожалуйста профиль",
        )
    people_id = people.id
    courses_id = people_and_groups_in.courses_id

    smtp = select(Groups).filter(Groups.courses_id == courses_id)
    result: Result = await session.execute(smtp)  # получаем резуллттат
    group = result.scalars().first()

    groups_id  = group.id

    stmt = (select(PeopleGroupsAssociation
                   ).filter(PeopleGroupsAssociation.people_id == people_id)
            .filter(PeopleGroupsAssociation.groups_id == groups_id))
    result: Result = await session.execute(stmt)  # получаем резуллттат
    pca = result.scalars().all()

    if pca:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Вы уже зачислены в группу по этим курсам",
        )

    # Создайте объект People с установленными user_id и status_id
    peoples_and_groups = PeopleGroupsAssociation(
        people_id=people_id,
        groups_id=groups_id
    )

    session.add(peoples_and_groups)
    await session.commit()
    await session.refresh(peoples_and_groups)  # обновляем данные перед возвратом
    return peoples_and_groups


async def get_one_peoples_and_groups(
        session: AsyncSession,
        user: User,
) -> List[Groups]:
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    temp_id = user.id

    smtp = select(People).filter(People.user_id == temp_id)
    result = await session.execute(smtp)
    people = result.scalars().first()

    people_id = people.id

    stmt = (
        select(Groups)
        .join(PeopleGroupsAssociation)
        .filter(PeopleGroupsAssociation.people_id == people_id)
    )

    result = await session.execute(stmt)
    groups = result.scalars().all()

    if not groups:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Группы не найдены для данного пользователя.",
        )

    return groups
