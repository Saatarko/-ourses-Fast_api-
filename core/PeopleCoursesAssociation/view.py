from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.exceptions import ResponseValidationError
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.PeopleCoursesAssociation.schemas import PeopleCoursesAssociationSchemas, PeopleCoursesAssociationSchemasCreate
from core.config import settings
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession
from core.PeopleCoursesAssociation import crud

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.peoplecoursesassociation,
    tags=["PeopleCoursesAssociation"],
)


@router.get("/", response_model=List[PeopleCoursesAssociationSchemas])
async def get_peoples_and_courses(
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    peoples_and_courses = await crud.get_peoples_and_courses(session=session)

    peoples_and_courses_schemas = [PeopleCoursesAssociationSchemas.from_orm(people) for people in peoples_and_courses]

    return peoples_and_courses_schemas


@router.post(
    "/{pk}",
    response_model=PeopleCoursesAssociationSchemas,
    status_code=status.HTTP_201_CREATED,
)
async def get_create_peoples_and_courses(
        pk: int,
        people_and_courses_in: PeopleCoursesAssociationSchemasCreate,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_peoples_and_courses(session=session,
                                                 people_and_courses_in=people_and_courses_in, pk=pk, user=user)
