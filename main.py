from contextlib import asynccontextmanager
from fastapi.responses import ORJSONResponse

import uvicorn
from fastapi import FastAPI, Path, Query, Body


from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()

main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)

# main_app.include_router(
#     api_router,
# )
# app.include_router(router=router_hero)  # включаем роутеры
# app.include_router(router=router_users)
# app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


if __name__ == "__main__":
    uvicorn.run(main_app)
