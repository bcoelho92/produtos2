"""empty message

Revision ID: ad30240a5df7
Revises: 63129e15aaac, b396c4493a7a
Create Date: 2023-09-21 09:19:51.508614

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad30240a5df7'
down_revision: Union[str, None] = ('63129e15aaac', 'b396c4493a7a')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
