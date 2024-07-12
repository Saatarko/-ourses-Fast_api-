from typing import TYPE_CHECKING

from sqlalchemy import Table, ForeignKey, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from .mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from .people import People
    from .courses import Courses


class PeopleCoursesAssociation(Base, IdIntPkMixin):
    __tablename__ = 'people_courses_association'
    __table_args__ = (
        UniqueConstraint('people_id', 'courses_id', name='idx_unic'),
    )
    people_id = Column(Integer, ForeignKey('people.id'))
    courses_id = Column(Integer, ForeignKey('courses.id'))