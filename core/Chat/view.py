from typing import List, Annotated, Optional

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import WebSocket, WebSocketDisconnect

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.Chat import crud
from core.Chat.schemas import ChatSchemas, ChatSchemasCreate, ChatGetList

from core.config import settings
from core.models import db_helper, User, user, AccessToken, Chat
from sqlalchemy.ext.asyncio import AsyncSession

import json

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.chat,
    tags=["Chat"],
)

clients: List[WebSocket] = []



@router.websocket("/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int,
                             session: AsyncSession = Depends(db_helper.scope_session_dependency)):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            # Получение сообщений от клиента
            data = await websocket.receive_text()
            data_json = json.loads(data)
            message = data_json.get("message")
            token = data_json.get("token")

            stmt = select(AccessToken).filter(AccessToken.token == token)
            result = await session.execute(stmt)
            temp_access_token = result.scalars().first()
            user_id = temp_access_token.user_id

            # Обработка входящих сообщений
            await crud.create_chat(group_id=chat_id, context=message, session=session, user_id=user_id)

            stmt = select(User).filter(User.id == user_id)
            result = await session.execute(stmt)
            temp_user = result.scalars().first()
            email = temp_user.email

            stmt = (select(Chat)
                    .filter(Chat.groups_id == chat_id)
                    .filter(Chat.user_id == user_id)
                    .filter(Chat.content == message)
                    .order_by(desc(Chat.id))
                    )

            result = await session.execute(stmt)
            temp_chat = result.scalars().first()
            time = temp_chat.timestamp

            # Отправка обновлений всем подключенным клиентам
            for client in clients:
                # Создание сообщения в формате JSON
                response_data = {
                    "message": message,
                    "email": email,
                    "time": time.isoformat(),  # Преобразование времени в строку ISO 8601
                    "chat_id": chat_id
                }
                await client.send_text(json.dumps(response_data))
    except WebSocketDisconnect:
        # Удаление клиента из списка при отключении
        clients.remove(websocket)


# @router.post(
#     "/",
#     response_model=ChatSchemas,
#     status_code=status.HTTP_201_CREATED,
# )
# async def create_chat(
#         chat_in: ChatSchemasCreate,
#         user: Annotated[User, Depends(current_user)],
#         session: AsyncSession = Depends(db_helper.scope_session_dependency),
# ):
#     return await crud.create_chat(session=session, chat_in=chat_in, user=user)


@router.get("/{pk}", response_model=List[ChatSchemas])
async def get_group_chat(
        pk: int,
        user: Annotated[User, Depends(current_user)],
        session: AsyncSession = Depends(db_helper.scope_session_dependency),
):
    chats = await crud.get_group_chat(session=session, pk=pk, user=user)

    # Преобразуем результаты в ChatSchemas
    chats_schemas = [ChatSchemas.from_orm(chat) for chat in chats]

    return chats_schemas
