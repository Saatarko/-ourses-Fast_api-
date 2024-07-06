from fastapi_users import FastAPIUsers

from core.models import User
from core.type.user_id import UserIdType
from api.dependencies.authentication import get_user_manager
from api.dependencies.authentication import auth_backend

# заготовка для маршрутов

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [auth_backend],
)
# две завыисисомти для текущий юзеров (для хи поулчения)
current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(active=True, superuser=True)
