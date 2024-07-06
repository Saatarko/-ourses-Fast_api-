from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    declared_attr,
)


class Base(DeclarativeBase):
    __abstract__ = True
    # базовый от которой  все таблицы налседуются (Сам не вносится в базу)

    @declared_attr.directive  # переопределение название таблицы(создается автоматом из навзания класса)
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
