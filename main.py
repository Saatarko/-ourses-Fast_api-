import os
import uvicorn
from contextlib import asynccontextmanager
from fastapi.responses import ORJSONResponse
from dotenv import load_dotenv

from fastapi import FastAPI, Path, Query, Body
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from upstash_redis import Redis


from core.models import db_helper
from api import router as api_router
from core.Courses.views import router as courses_router
from core.Status.view import router as status_router
from core.People.view import router as people_router
from core.PeopleCoursesAssociation.view import router as people_courses_router
from core.Groups.view import router as groups_router
from core.PeopleGroupsAssociation.view import router as people_groups_router
from core.Lessons.view import router as lessons_router
from core.Chat.view import router as chat_router
from core.Test.view import router as test_router

load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    redis_url = os.getenv("UPSTASH_REDIS_URL", "https://deciding-scorpion-49624.upstash.io")
    redis_token = os.getenv("UPSTASH_REDIS_TOKEN", "AcHYAAIjcDFmZjIxOTE3YmVhMmI0NDlkYTg3YjJjNGUyMTEyMzNmMnAxMA")

    redis_client = Redis(url=redis_url, token=redis_token)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")

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
main_app.include_router(
    status_router,
)

main_app.include_router(
    people_router,
)

main_app.include_router(
    people_courses_router,
)

main_app.include_router(
    groups_router,
)
main_app.include_router(
    people_groups_router,
)
main_app.include_router(
    lessons_router,
)
main_app.include_router(
    chat_router,
)

main_app.include_router(
    test_router,
)
#
if __name__ == "__main__":
    uvicorn.run("main:main_app", host="127.0.0.1", port=8000, reload=True)
    # uvicorn.run(main_app)
