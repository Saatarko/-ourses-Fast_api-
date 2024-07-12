from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class PeopleSchemas(BaseModel):
    first_name: str = Field(..., max_length=30, min_length=3)
    last_name: str = Field(..., max_length=30, min_length=3)
    age:int

    class Config:
        from_attributes = True


class Peoples(PeopleSchemas):  #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class PeopleSchemasCreate(PeopleSchemas):  #  создание
    pass
