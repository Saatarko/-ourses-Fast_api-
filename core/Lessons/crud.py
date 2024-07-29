import asyncio
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.Lessons.schemas import LessonsSchemasCreate, LessonList
from core.models import User, Groups, PeopleCoursesAssociation, Lessons
from sqlalchemy.engine import Result
from api.api_v1.fastapi_user_routers import current_user
from core.schemas.user import UserRead


async def create_lessons(
        session: AsyncSession,
        lesson_in: LessonsSchemasCreate,
        user: User
) -> Lessons:
    # Проверка, залогинен ли пользователь
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    lesson = Lessons(
        title=lesson_in.title,
        document_path=lesson_in.document_path,
        courses_id=lesson_in.courses_id
    )

    session.add(lesson)
    await session.commit()
    await session.refresh(lesson)  # обновляем данные перед возвратом
    return lesson


async def get_lessons(session: AsyncSession, user: User) -> list[Lessons]:  # ожидаем список людей

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    stmt = select(Lessons).order_by(Lessons.id)  # получаем списолк
    result: Result = await session.execute(stmt)  # получаем резуллттат
    lesson = result.scalars().all()
    return list(lesson)


@cache(expire=60*60)
async def get_list_lessons(session: AsyncSession, lesson_in: LessonList) -> list[Lessons]:

    temp_id = lesson_in.id
    stmt = select(Groups).filter(Groups.id == temp_id).order_by(Groups.id)
    result: Result = await session.execute(stmt)
    group = result.scalars().first()

    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Group not found",
        )

    temp_courses_id = group.courses_id

    stmt = select(Lessons).filter(Lessons.courses_id == temp_courses_id).order_by(Lessons.id)
    result: Result = await session.execute(stmt)
    lessons = result.scalars().all()
    return list(lessons)
