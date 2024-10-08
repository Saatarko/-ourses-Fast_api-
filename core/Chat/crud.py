import asyncio
from datetime import datetime, timedelta
from typing import Annotated, List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from core.Chat.schemas import ChatSchemasCreate, ChatGetList
from core.models import User, Chat, AccessToken
from sqlalchemy.engine import Result
from api.api_v1.fastapi_user_routers import current_user
from core.schemas.user import UserRead
from fastapi_users import schemas


async def create_chat(
        session: AsyncSession,
        context: str,
        user_id: int,
        group_id: int,
) -> Chat:
    # Проверка, залогинен ли пользователь

    # Создаем объект группы
    chat = Chat(
        content=context,
        groups_id=group_id,
        user_id=user_id,
    )

    # Добавление группы в сессию и коммит
    session.add(chat)
    await session.commit()
    await session.refresh(chat)  # Обновляем объект группы для получения id и других значений из БД

    return chat

# async def create_chat(
#         session: AsyncSession,
#         chat_in: ChatSchemasCreate,
#         user: User
# ) -> Chat:
#     # Проверка, залогинен ли пользователь
#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Not authenticated",
#         )
#
#     user_id = user.id
#
#     # Создаем объект группы
#     chat = Chat(
#         content=chat_in.content,
#         groups_id=chat_in.groups_id,
#         user_id=user_id,
#     )
#
#     # Добавление группы в сессию и коммит
#     session.add(chat)
#     await session.commit()
#     await session.refresh(chat)  # Обновляем объект группы для получения id и других значений из БД
#
#     return chat



async def get_group_chat(
        pk: int,
        session: AsyncSession,
        user: User
) -> List[Chat]:  # Изменили возвращаемый тип на List[Chat]

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    now = datetime.now() - timedelta(days=7)

    # Изменяем запрос для загрузки связанных данных из таблицы Groups
    stmt = (
        select(Chat)
        .options(selectinload(Chat.user))  # Подгружаем связанные данные из таблицы Groups
        .filter(Chat.groups_id == pk)
        .filter(Chat.timestamp > now)
        .order_by(Chat.timestamp)
    )

    result = await session.execute(stmt)
    chats = result.scalars().all()

    return chats


# async def get_user_from_token(token: str, session: AsyncSession) -> Optional[schemas.BaseUserCreate]:
#     # Найти AccessToken по токену
#     stmt = select(AccessToken).filter(AccessToken.token == token)
#     result = await session.execute(stmt)
#     temp = result.scalars().first()
#
#     if temp is None:
#         # Если токен не найден, возвращаем None
#         return None
#
#     user_id = temp.user_id  # Предполагаем, что у AccessToken есть поле user_id
#
#     # Найти User по user_id
#     stmt = select(User).filter(User.id == user_id)
#     result = await session.execute(stmt)
#     user = result.scalars().first()
#
#     return user