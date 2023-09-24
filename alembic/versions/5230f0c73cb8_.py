"""empty message

Revision ID: 5230f0c73cb8
Revises: 20eed46c4422
Create Date: 2023-09-22 10:57:01.448490

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5230f0c73cb8'
down_revision: Union[str, None] = '20eed46c4422'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
