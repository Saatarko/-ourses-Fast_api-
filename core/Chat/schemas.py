from datetime import datetime
from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict



class ChatSchemas(BaseModel):
    content: str = Field(..., max_length=500)
    groups_id: int
    user_id: int

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