from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class StatusSchemas(BaseModel):
    name: str = Field(..., max_length=30, min_length=3)
    class Config:
        from_attributes = True


class Status(StatusSchemas):  #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class StatusSchemasCreate(StatusSchemas):  #  создание
    pass
