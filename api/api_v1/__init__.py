from fastapi import APIRouter

from core.config import settings
from .auth import router as auth_router

router = APIRouter(
    prefix=settings.api_v1_prefix,
)
router.include_router(auth_router)
