from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser
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
async def get_courses(
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
    user: User = Depends(current_superuser),
):

    courses = await crud.get_courses(session=session)
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas
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
