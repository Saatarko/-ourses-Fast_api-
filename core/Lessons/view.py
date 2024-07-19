from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.Lessons.schemas import LessonsSchemas, LessonsSchemasCreate, LessonList
from core.config import settings
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession
from core.Lessons import crud


from typing import List



router = APIRouter(
    prefix=settings.api.v1.lessons,
    tags=["Lessons"],
)


@router.get("/", response_model=List[LessonsSchemas])
async def get_lessons(
    user: Annotated[User, Depends(current_user)],
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):

    lessons = await crud.get_lessons(session=session, user=user)
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas
    lessons_schemas = [LessonsSchemas.from_orm(lesson) for lesson in lessons]

    return lessons_schemas

@router.post("/list", response_model=List[LessonsSchemas])
async def get_list_lessons(
    user: Annotated[User, Depends(current_user)],
    lesson_in: LessonList,
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):

    lessons = await crud.get_list_lessons(session=session, lesson_in=lesson_in,user=user)
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas
    lessons_schemas = [LessonsSchemas.from_orm(lesson) for lesson in lessons]

    return lessons_schemas


@router.post(
    "/",
    response_model=LessonsSchemasCreate,
    status_code=status.HTTP_201_CREATED,
)
async def create_lessons(
    user: Annotated[User, Depends(current_user)],
    lesson_in: LessonsSchemasCreate,
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_lessons(session=session, lesson_in=lesson_in, user=user)