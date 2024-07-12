from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models.mixins.id_int_pk import IdIntPkMixin
from core.models import Base, User, Status, Courses

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession
    from core.models import Base, User, Status, Courses


class People(Base, IdIntPkMixin):
    first_name = Column(String(30))
    last_name = Column(String(30))
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'), unique=True)
    user = relationship('User', back_populates='people')
    status_id = Column(Integer, ForeignKey('status.id'), unique=True)
    status = relationship('Status', back_populates='people')
    courses = relationship(
        'Courses',
        secondary='people_courses_association',
        back_populates='people'
    )