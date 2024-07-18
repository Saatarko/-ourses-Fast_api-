from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Column, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins.id_int_pk import IdIntPkMixin
from core.models import Base

if TYPE_CHECKING:
    from core.models import Base, Groups


class Chat(Base, IdIntPkMixin):
    chaters = Column(String(30))
    content = Column(String(500))
    timestamp = Column(DateTime, default=func.now())

    groups_id = Column(Integer, ForeignKey('groups.id'))
    groups = relationship('Groups', back_populates='chat')
