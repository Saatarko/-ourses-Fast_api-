from pydantic import BaseModel
from pydantic_settings import BaseSettings

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "my.dbsqlite3"


class DbSetting(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = False


# имеется путь относительно текущего файла, просто parent- core, .parent.parent - уже проект
class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    # db_echo: bool = True  # отображает sql запросы в консоле
    db: DbSetting = DbSetting()


settings = Settings()
