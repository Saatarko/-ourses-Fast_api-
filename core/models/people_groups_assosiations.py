from typing import TYPE_CHECKING

from sqlalchemy import Table, ForeignKey, Column, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base
from .mixins.id_int_pk import IdIntPkMixin

if TYPE_CHECKING:
    from .people import People
    from .groups import Groups


class PeopleGroupsAssociation(Base, IdIntPkMixin):
    __tablename__ = 'people_groups_association'
    __table_args__ = (
        UniqueConstraint('people_id', 'groups_id', name='idx_unic'),
    )
    people_id = Column(Integer, ForeignKey('people.id'))
    groups_id = Column(Integer, ForeignKey('groups.id'))

