from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class LessonsSchemas(BaseModel):
    title: str = Field(..., max_length=30, min_length=3)
    document_path: str = Field(..., max_length=100, min_length=3)
    courses_id: int
    id: int
    class Config:
        from_attributes = True

class LessonList(BaseModel):  #  данные для вывода чтобы id не выводиь вместе со всеми
    id: int

    class Config:
        from_attributes = True


class Lesson(LessonsSchemas):  #  данные для вывода чтобы id не выводиь вместе со всеми
    id: int

    class Config:
        from_attributes = True


class LessonsSchemasCreate(LessonsSchemas):  #  создание
    pass


