"""empty message

Revision ID: 267a52214fb3
Revises: ec5294afb0de
Create Date: 2023-09-22 10:54:14.202391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '267a52214fb3'
down_revision: Union[str, None] = 'ec5294afb0de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
