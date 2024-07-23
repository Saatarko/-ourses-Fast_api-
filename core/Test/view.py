from typing import List, Annotated

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.fastapi_user_routers import current_superuser, current_user
from core.config import settings
from core.models import db_helper, User
from sqlalchemy.ext.asyncio import AsyncSession

# if TYPE_CHECKING:


from typing import List

from core.schemas.user import UserRead

router = APIRouter(
    prefix=settings.api.v1.test,
    tags=["Tests"],
)


