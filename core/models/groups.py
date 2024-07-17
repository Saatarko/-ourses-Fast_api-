from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins.id_int_pk import IdIntPkMixin
from core.models import Base

if TYPE_CHECKING:

    from core.models import Base, Courses, Chat


class Groups(Base, IdIntPkMixin):
    name = Column(String(30))
    date_start = Column(String(30))

    courses_id = Column(Integer, ForeignKey('courses.id'))
    courses = relationship('Courses', back_populates='groups')

    people = relationship('People', back_populates='groups')

    chat_id = Column(Integer, ForeignKey('chat.id'))
    chat = relationship('Chat', back_populates='groups')

