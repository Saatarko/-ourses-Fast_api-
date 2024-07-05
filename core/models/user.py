from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from core.models import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import (AsyncSession)

# объявление класса user из fast-api users
class User(SQLAlchemyBaseUserTable[int], Base):

    # объявление метода получения юзера
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, User)
