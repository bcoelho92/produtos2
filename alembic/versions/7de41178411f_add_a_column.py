"""Add a column

Revision ID: 7de41178411f
Revises: f1fabb7f4fb5
Create Date: 2023-09-05 09:10:34.591602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7de41178411f'
down_revision: Union[str, None] = 'f1fabb7f4fb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
