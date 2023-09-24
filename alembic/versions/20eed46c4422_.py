"""empty message

Revision ID: 20eed46c4422
Revises: 267a52214fb3
Create Date: 2023-09-22 10:56:46.630355

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20eed46c4422'
down_revision: Union[str, None] = '267a52214fb3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
