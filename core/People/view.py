from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.exceptions import ResponseValidationError
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.People.schemas import PeopleSchemas, PeopleSchemasCreate, PeopleSchemasUpdate, PeopleSchemasAddGroupe
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
    if people:
        return people
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден",
        )


@router.put("/update/{pk}", response_model=PeopleSchemasUpdate)
async def update_one_people(
        pk: int,
        people_in: PeopleSchemasUpdate,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    people = await crud.update_one_people(session=session, pk=pk, user=user, people_in=people_in)
    return people


@router.get("/add_student", response_model=PeopleSchemasAddGroupe)
async def get_add_student(
        people_in: PeopleSchemasAddGroupe,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    # Преобразование списка курсов в список объектов, соответствующих схеме CoursesSchemas
    people = await crud.add_student(session=session, user=user, people_in=people_in)

    return people
