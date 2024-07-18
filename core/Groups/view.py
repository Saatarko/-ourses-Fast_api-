from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.Groups import crud
from core.Groups.schemas import GroupsSchemas, GroupsSchemasCreate

from core.config import settings
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.groups,
    tags=["Groups"],
)


@router.post(
    "/",
    response_model=GroupsSchemas,
    status_code=status.HTTP_201_CREATED,
)
async def get_create_groups(
        groupe_in: GroupsSchemasCreate,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_groups(session=session, groupe_in=groupe_in, user=user)



@router.get("/", response_model=List[GroupsSchemas])
async def get_courses(
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    groups = await crud.get_groups(session=session, user=user)
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas
    groups_schemas = [GroupsSchemas.from_orm(group) for group in groups]

    return groups_schemas
