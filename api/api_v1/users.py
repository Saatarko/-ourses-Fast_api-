from fastapi import APIRouter

from core.schemas.user import UserRead, UserUpdate
from .fastapi_user_routers import fastapi_users
from core.config import settings

# создаем роутеры для аутентификации пользователя


router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Users"],
)

# '/me'  /{id}
router.include_router(
    fastapi_users.get_users_router(
        UserRead,
        UserUpdate,
    ),
)
