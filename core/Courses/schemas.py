from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class CoursesSchemas(BaseModel):
    name: str = Field(..., max_length=30, min_length=3)
    description: Annotated[
        str, MinLen(5), MaxLen(1000)
    ]  # два разных метода обозначения валидации
    price: int
    id: int

    class Config:
        from_attributes = True


class Courses(CoursesSchemas):  #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class CoursesSchemasCreate(CoursesSchemas):  #  создание
    pass
