from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
    AsyncSession,
)
from sqlalchemy.orm import sessionmaker

from core.config import settings
from asyncio import current_task


class DatabaseHelper:  # базы данных, плюс фабрика сессий

    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,  # агрузим движек в сесиинмейкер
            autoflush=False,  # автоподготовка  к коммиту
            autocommit=False,  # авто коммит
            expire_on_commit=False,
        )

    def get_scope_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def scope_session_dependency(self) -> AsyncSession:
        session = self.get_scope_session()
        yield session
        await session.close()

    async def session_dependency(self) -> AsyncSession:
        async with self.session_factory() as session:
            yield session
            await session.close()

    # async def dispose(self) -> None:
    #     await self.engine.dispose()
    #
    # async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
    #     async with self.session_factory() as session:
    #         yield session


db_helper = DatabaseHelper(
    url=settings.db.url,
    echo=settings.db.echo,
)
