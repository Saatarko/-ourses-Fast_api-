from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class PeopleCoursesAssociationSchemas(BaseModel):
    courses_id: int

    class Config:
        from_attributes = True


class PeopleCoursesAssociation(PeopleCoursesAssociationSchemas):
    #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class PeopleCoursesAssociationSchemasCreate(PeopleCoursesAssociationSchemas):  #  создание
    pass


class PeopleCoursesAssociationSchemasUpdate(PeopleCoursesAssociationSchemas):  #  создание
    pass
