from typing import TYPE_CHECKING

from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin


if TYPE_CHECKING:
    from core.models import People

class Courses(Base, IdIntPkMixin):
    name = Column(String(30))
    description = Column(String(100))
    price = Column(Integer)
    people = relationship(
        'People',
        secondary='people_courses_association',
        back_populates='courses'
    )