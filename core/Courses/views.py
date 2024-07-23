from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi_cache import FastAPICache
from fastapi_cache.decorator import cache
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.Courses import crud
from core.Courses.schemas import CoursesSchemas, CoursesSchemasCreate, Courses
from core.config import settings
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.courses,
    tags=["Courses"],
)

@router.get("/", response_model=List[CoursesSchemas])
@cache(expire=60 * 30)  # Используйте декоратор cache для кэширования на 30 минут
async def get_courses(
    user: Annotated[User, Depends(current_user)],
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    courses = await crud.get_courses(session=session)
    courses_schemas = [CoursesSchemas.from_orm(course) for course in courses]
    return courses_schemas




# @router.get("/", response_model=List[CoursesSchemas])
# async def get_courses(
#     session: AsyncSession = Depends(db_helper.scope_session_dependency),
# ):
#     return await crud.get_courses(session=session)


@router.post(
    "/",
    response_model=CoursesSchemas,
    status_code=status.HTTP_201_CREATED,
)
async def get_create_courses(
    courses_in: CoursesSchemasCreate,
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_courses(session=session, courses_in=courses_in)
