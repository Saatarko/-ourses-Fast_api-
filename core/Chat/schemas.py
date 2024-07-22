from datetime import datetime
from typing import Annotated, Optional

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict

from core.Groups.schemas import GroupsSchemas
from core.schemas.user import UserRead


class ChatSchemas(BaseModel):
    content: str = Field(..., max_length=500)
    user_id: int
    user: Optional[UserRead]  # Изменено на groups для включения данных о группе
    timestamp: datetime  # Указываем тип как datetime
    id: int

    class Config:
        from_attributes = True

class Chat(ChatSchemas):  #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class ChatSchemasCreate(BaseModel):  #  создание
    content: str = Field(..., max_length=500)
    groups_id: int

    class Config:
        from_attributes = True



class ChatGetList(BaseModel):
    pass