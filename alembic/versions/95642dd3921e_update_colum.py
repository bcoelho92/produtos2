"""update colum

Revision ID: 95642dd3921e
Revises: ad30240a5df7
Create Date: 2023-09-21 09:19:58.260861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95642dd3921e'
down_revision: Union[str, None] = 'ad30240a5df7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
