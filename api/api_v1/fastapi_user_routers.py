from fastapi_users import FastAPIUsers

from core.models import User
from core.type.user_id import UserIdType
from api.dependencies.authentication.user_manager import get_user_manager
from api.dependencies.authentication.backend import auth_backend

# заготовка для маршрутов

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [auth_backend],
)
