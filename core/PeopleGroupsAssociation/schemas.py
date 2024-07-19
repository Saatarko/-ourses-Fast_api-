from typing import Annotated

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel, Field, ConfigDict


class PeopleGroupsAssociationSchemas(BaseModel):
    courses_id: int

    class Config:
        from_attributes = True


class PeopleGroupsAssociationSchemasResponse(BaseModel):
    people_id: int
    groups_id: int
    # courses_id здесь не будет, так как он не нужен в ответе

    class Config:
        from_attributes = True
class PeopleGroupsAssociation(PeopleGroupsAssociationSchemas):
    #  данные для вывода чтобы id не выводиь вместе со всеми
    model_config = ConfigDict(from_attributes=True)
    id: int


class PeopleGroupsAssociationSchemasCreate(PeopleGroupsAssociationSchemas):  #  создание
    pass


class PeopleGroupsAssociationSchemasUpdate(PeopleGroupsAssociationSchemas):  #  создание
    pass
