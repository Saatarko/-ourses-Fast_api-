
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


from core.models import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    pass
