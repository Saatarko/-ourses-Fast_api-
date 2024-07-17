from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins.id_int_pk import IdIntPkMixin
from core.models import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from core.models import People


class Status(Base, IdIntPkMixin):
    name = Column(String(30), unique=True, index=True)

    people = relationship('People', back_populates='status')
