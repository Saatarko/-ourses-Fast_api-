from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class GroupsSchemas(BaseModel):
    name: str = Field(..., max_length=30, min_length=3)
    courses_id: int

    class Config:
        from_attributes = True


class Groups(GroupsSchemas):  #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class GroupsSchemasCreate(GroupsSchemas):  #  создание
    pass


class GroupsSchemasTakeOne(BaseModel):  #  создание
    name: str