from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins.id_int_pk import IdIntPkMixin
from core.models import Base

if TYPE_CHECKING:

    from core.models import Base, Courses


class Lessons(Base, IdIntPkMixin):
    title = Column(String(30))
    document_path = Column(String(100))

    courses_id = Column(Integer, ForeignKey('courses.id'))
    courses = relationship('Courses', back_populates='lessons')

