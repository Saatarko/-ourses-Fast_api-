from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from core.models import User, db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import (AsyncSession)

# модель для стратегии на получение users
async def get_user_db(
        session: Annotated['AsyncSession',
        Depends(db_helper.session_getter),
        ],
):
    yield User.get_db(session=session)
