from contextlib import asynccontextmanager
from fastapi.responses import ORJSONResponse

import uvicorn
from fastapi import FastAPI, Path, Query, Body

from core.models import db_helper
from api import router as api_router
from core.Courses.views import router as courses_router


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

main_app.include_router(
    api_router,
)
main_app.include_router(
    courses_router,
)


if __name__ == "__main__":
    uvicorn.run("main:main_app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(main_app)
