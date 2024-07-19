from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.exceptions import ResponseValidationError
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.PeopleGroupsAssociation.schemas import PeopleGroupsAssociationSchemas, PeopleGroupsAssociationSchemasResponse, \
    PeopleGroupsAssociationSchemasCreate, OnePeopleGroupsSchemasResponse
from core.config import settings
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession
from core.PeopleGroupsAssociation import crud

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.peoplegroupesassociation,
    tags=["Peoplegroupesassociation"],
)


@router.get("/", response_model=List[PeopleGroupsAssociationSchemas])
async def get_peoples_and_groups(
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    peoples_and_groups = await crud.get_peoples_and_groups(session=session)

    peoples_and_groups_schemas = [PeopleGroupsAssociationSchemas.from_orm(people) for people in peoples_and_groups]

    return peoples_and_groups_schemas


@router.get("/check", response_model=List[OnePeopleGroupsSchemasResponse])
async def get_one_peoples_and_groups(
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    groups = await crud.get_one_peoples_and_groups(session=session, user=user)

    # ``groups`` это список объектов `Groups`
    groups_schemas = [OnePeopleGroupsSchemasResponse.from_orm(group) for group in groups]

    return groups_schemas



@router.post(
    "/",
    response_model=PeopleGroupsAssociationSchemasResponse,
    status_code=status.HTTP_201_CREATED,
)
async def get_create_peoples_and_groups(
        people_and_groups_in: PeopleGroupsAssociationSchemasCreate,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_peoples_and_groups(session=session,
                                                 people_and_groups_in=people_and_groups_in, user=user)
