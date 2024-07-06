from fastapi import APIRouter

from api.api_v1.fastapi_user_routers import fastapi_users
from api.dependencies.authentication import auth_backend
from core.config import settings
from core.schemas.user import UserRead, UserCreate

# создаем роутеры для аутентификации пользователя

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

# добаавляем пути /login и /logout
router.include_router(
    router=fastapi_users.get_auth_router(
        auth_backend,
        # requires_verification=True  # требуется верефикация почты для входа
    ),
)


# /register доавбляем

router.include_router(
    router=fastapi_users.get_register_router(
        UserRead,
        UserCreate,
    )
)

# /request-verify-token and /verify
router.include_router(
    router=fastapi_users.get_verify_router(UserRead),
)

# /forgot-password and /reset-password
router.include_router(
    router=fastapi_users.get_reset_password_router(),
)
