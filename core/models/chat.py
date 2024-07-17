from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Column, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins.id_int_pk import IdIntPkMixin
from core.models import Base

if TYPE_CHECKING:

    from core.models import Base


class Chat(Base, IdIntPkMixin):
    chaters = Column(String(30))
    content = Column(String(500))
    timestamp = Column(DateTime, default=func.now())


    courses_id = Column(Integer, ForeignKey('courses.id'))
    courses = relationship('Courses', back_populates='lessons')

