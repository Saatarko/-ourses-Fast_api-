from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.People.schemas import PeopleSchemas, PeopleSchemasCreate, PeopleSchemasUpdate
from core.config import settings
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession
from core.People import crud

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.people,
    tags=["People"],
)


@router.get("/", response_model=List[PeopleSchemas])
async def get_people(
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    peoples = await crud.get_people(session=session)
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas
    people_schemas = [PeopleSchemas.from_orm(people) for people in peoples]

    return people_schemas


@router.post(
    "/",
    response_model=PeopleSchemas,
    status_code=status.HTTP_201_CREATED,
)
async def get_create_people(
        people_in: PeopleSchemasCreate,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    return await crud.create_people(session=session, people_in=people_in, user=user)


@router.get("/{pk}", response_model=PeopleSchemas)
async def get_one_people(
        pk: int,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    people = await crud.get_one_people(session=session, pk=pk, user=user)
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas

    return people

@router.put("/update/{pk}", response_model=PeopleSchemasUpdate)
async def update_one_people(
        pk: int,
        people_in: PeopleSchemasUpdate,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    people = await crud.update_one_people(session=session, pk=pk, user=user, people_in=people_in)
    return people