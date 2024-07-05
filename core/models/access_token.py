from typing import AsyncGenerator

from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, ForeignKey

from .base import Base
from core.type.user_id import UserIdType


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable[UserIdType]):

    user_id: Mapped[UserIdType] = mapped_column(
        GUID, ForeignKey("user.id", ondelete="cascade"), nullable=False
    )


async def get_access_token_db(
        session: AsyncSession = Depends(get_async_session),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
