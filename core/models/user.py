from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.models import Base
from core.type.user_id import UserIdType


if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import (AsyncSession)

# объявление класса user из fast-api users
class User(Base, SQLAlchemyBaseUserTable[UserIdType]):

    # объявление метода получения юзера
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
