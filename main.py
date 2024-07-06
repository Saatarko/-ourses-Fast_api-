from contextlib import asynccontextmanager
from fastapi.responses import ORJSONResponse

import uvicorn
from fastapi import FastAPI, Path, Query, Body

from core.models import db_helper
from api import router as api_router


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

if __name__ == "__main__":
    uvicorn.run(main_app)
