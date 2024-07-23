from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import WebSocket, WebSocketDisconnect

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.Chat import crud
from core.Chat.schemas import ChatSchemas, ChatSchemasCreate, ChatGetList

from core.config import settings
from core.models import db_helper, User, user
from sqlalchemy.ext.asyncio import AsyncSession

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.chat,
    tags=["Chat"],
)

clients: List[WebSocket] = []


@router.websocket("/{chat_id}")
async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            # Получение сообщений от клиента
            data = await websocket.receive_text()
            # Обработка входящих сообщений
            await crud.create_chat(chat_id=chat_id, chat_in=data, user=user)

            # Отправка обновлений всем подключенным клиентам
            for client in clients:
                if client != websocket:
                    await client.send_text(f"New message in chat {chat_id}: {data}")
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
