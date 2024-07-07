import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.Courses.schemas import CoursesSchemas, CoursesSchemasCreate
from core.models import Courses
from sqlalchemy.engine import Result


async def create_courses(
    session: AsyncSession, courses_in: CoursesSchemasCreate
) -> Courses:
    courses = Courses(**courses_in.model_dump())
    session.add(courses)
    await session.commit()
    await session.refresh(
        courses
    )  # обновляем данные перед возвратом ибо двигло асинхронное малоли шо
    return courses


async def get_courses(session: AsyncSession) -> list[Courses]:  # ожидаем список курсов
    stmt = select(Courses).order_by(Courses.id)  # получаем списолк игроков из базы
    result: Result = await session.execute(stmt)  # получаем резуллттат
    courses = result.scalars().all()
    return list(courses)
