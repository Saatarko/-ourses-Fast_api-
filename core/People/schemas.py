from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class PeopleSchemas(BaseModel):
    first_name: str = Field(..., max_length=30, min_length=3)
    last_name: str = Field(..., max_length=30, min_length=3)
    age:int

    class Config:
        from_attributes = True


class PeopleCheckResponceSchemas(BaseModel):
    courses_and_groups_check: dict

class Peoples(PeopleSchemas):  #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class PeopleSchemasCreate(PeopleSchemas):  #  создание
    pass

class PeopleSchemasUpdate(PeopleSchemas):  #  создание
    pass


class PeopleSchemasAddGroupe(PeopleSchemas):  #  создание
    # groups_id: int
    groupe_name: str

