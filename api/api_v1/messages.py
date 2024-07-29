from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from core.schemas.user import UserRead
from .fastapi_user_routers import current_user, current_superuser
from core.config import settings
from core.models import User

router = APIRouter(
    prefix=settings.api.v1.messages,
    tags=["Messages"],
)


@router.get("")
def get_user_messages(
    user: Annotated[
        User,
        Depends(current_user),
    ]
):
    return {
        "messages": ["m1", "m2", "m3"],
        "user": UserRead.model_validate(user),  # получение текущего юзера в json
    }


@router.get("/secrets")
def get_superuser_messages(
    user: Annotated[
        User,
        Depends(current_superuser),
    ]
):
    return {
        "messages": ["secrets-m1", "secrets-m2", "secrets-m3"],
        "user": UserRead.model_validate(user),  # получение текущего юзера в json
    }

@router.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"}, status_code=200)
