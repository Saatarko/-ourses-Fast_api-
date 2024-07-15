"""Remove unique constraint from status_id

Revision ID: f0fb8450778b
Revises: 2fc9f7926d08
Create Date: 2024-07-15 16:37:08.712645

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f0fb8450778b"
down_revision: Union[str, None] = "2fc9f7926d08"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Удаление уникального ограничения
    with op.batch_alter_table('people') as batch_op:
        batch_op.drop_constraint('uq_people_status_id', type_='unique')

def downgrade():
    # Восстановление уникального ограничения
    with op.batch_alter_table('people') as batch_op:
        batch_op.create_unique_constraint('uq_people_status_id', ['status_id'])
