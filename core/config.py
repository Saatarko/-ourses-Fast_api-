from pydantic import BaseModel
from pydantic_settings import BaseSettings

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "my.dbsqlite3"


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
    api_v1_prefix: str = "/api/v1"

    # db_echo: bool = True  # отображает sql запросы в консоле
    db: DbSetting = DbSetting()


settings = Settings()
