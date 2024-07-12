from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser
from core.Status.schemas import StatusSchemas, StatusSchemasCreate
from core.config import settings
from core.models import Courses, db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession
from core.Status import crud

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.status,
    tags=["Status"],
)


@router.get("/", response_model=List[StatusSchemas])
async def get_courses(
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):

    statuses = await crud.get_status(session=session)
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas
    statuses_schemas = [StatusSchemas.from_orm(status) for status in statuses]

    return statuses_schemas


@router.post(
    "/",
    response_model=StatusSchemas,
    status_code=status.HTTP_201_CREATED,
)
async def get_create_status(
    status_in: StatusSchemasCreate,
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_status(session=session, status_in=status_in)