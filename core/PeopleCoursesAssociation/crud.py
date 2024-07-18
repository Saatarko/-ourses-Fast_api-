import asyncio
from typing import Annotated

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.PeopleCoursesAssociation.schemas import PeopleCoursesAssociationSchemasCreate
from core.models import User, PeopleCoursesAssociation, People
from sqlalchemy.engine import Result
from api.api_v1.fastapi_user_routers import current_user
from core.schemas.user import UserRead


async def get_peoples_and_courses(session: AsyncSession) -> list[PeopleCoursesAssociation]:  # ожидаем список людей
    stmt = select(PeopleCoursesAssociation).order_by(PeopleCoursesAssociation.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    people_and_courses = result.scalars().all()
    return list(people_and_courses)


async def create_peoples_and_courses(

        session: AsyncSession,
        people_and_courses_in: PeopleCoursesAssociationSchemasCreate,
        user: User,
        pk: int,

) -> PeopleCoursesAssociation:
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
    courses_id = pk

    stmt = (select(PeopleCoursesAssociation
                   ).filter(PeopleCoursesAssociation.people_id == people_id)
            .filter(PeopleCoursesAssociation.courses_id == courses_id))
    result: Result = await session.execute(stmt)  # получаем резуллттат
    pca = result.scalars().all()

    if pca:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Вы уже записаны на эти курсы",
        )

    # Создайте объект People с установленными user_id и status_id
    peoples_and_courses = PeopleCoursesAssociation(
        people_id=people_id,
        courses_id=courses_id
    )

    session.add(peoples_and_courses)
    await session.commit()
    await session.refresh(peoples_and_courses)  # обновляем данные перед возвратом
    return peoples_and_courses
