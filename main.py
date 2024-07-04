from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Path, Query, Body

from core.config import settings


@asynccontextmanager  # функция действий до запуска приложения (сейчас функция пустая)
async def lifespan(app: FastAPI):
    yield
    # действия на события по удалению до запуска


my_app = FastAPI(lifespan=lifespan)
# app.include_router(router=router_hero)  # включаем роутеры
# app.include_router(router=router_users)
# app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run(my_app)
