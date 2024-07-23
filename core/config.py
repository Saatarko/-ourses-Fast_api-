from pydantic import BaseModel
from pydantic_settings import BaseSettings

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


DB_PATH = BASE_DIR / "my.dbsqlite3"

UPLOAD_DIR = "uploads/"


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    auth: str = "/auth"
    users: str = "/users"
    messages: str = "/messages"
    courses: str = "/courses"
    status: str = "/status"
    people: str = "/people"
    peoplecoursesassociation: str = '/peoplecoursesassociation'
    groups: str = '/groups'
    peoplegroupesassociation: str = '/peoplegroupesassociation'
    lessons: str = '/lessons'
    chat: str = '/chat'
    test: str = '/test'


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()

    @property
    def bearer_token_url(self) -> str:
        # соединяем api/v1/auth/login
        parts = (self.prefix, self.v1.prefix, self.v1.auth, "/login")
        path = "".join(parts)
        # return path[1:]
        return path.removeprefix("/")


class AccessToken(BaseModel):
    lifetime_second: int = 3600
    reset_password_token_secret: str = (
        "15eddcf6f24f18ba2f4f7286fee40acd7a16e3d8d832ce7feb28638825d056ff"
    )
    verification_token_secret: str = (
        "2497496b444b2b2caf34463ab3ca20b7c670c5331d01a2c3c8e1358dc4e9745d"
    )


class DbSetting(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = False
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


# имеется путь относительно текущего файла, просто parent- core, .parent.parent - уже проект
class Settings(BaseSettings):
    api: ApiPrefix = ApiPrefix()

    # db_echo: bool = True  # отображает sql запросы в консоле
    db: DbSetting = DbSetting()
    access_token: AccessToken = AccessToken()


settings = Settings()
