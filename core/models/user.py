from typing import TYPE_CHECKING

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.orm import Mapped, relationship

from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin

from core.type.user_id import UserIdType

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from core.models.people import People


# объявление класса user из fast-api users
class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[UserIdType]):

    # объявление метода получения юзера
    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)

    people: Mapped['People'] = relationship('People', back_populates='user', uselist=False)
