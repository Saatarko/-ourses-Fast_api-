from typing import TYPE_CHECKING

from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from core.models import People, Groups, Lessons, Chat


class Courses(Base, IdIntPkMixin):
    name = Column(String(30))
    description = Column(String(1000))
    price = Column(Integer)

    groups = relationship('Groups', back_populates='courses')

    lessons = relationship('Lessons', back_populates='courses')


    people = relationship(
        'People',
        secondary='people_courses_association',
        back_populates='courses'
    )
