from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from core.type.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import (AsyncSession)


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):
    user_id: Mapped[UserIdType] = mapped_column(
        Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False
    )

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyAccessTokenDatabase(session, cls)
