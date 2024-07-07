from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins.id_int_pk import IdIntPkMixin


class Courses(Base, IdIntPkMixin):

    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(100))
    price: Mapped[int]
