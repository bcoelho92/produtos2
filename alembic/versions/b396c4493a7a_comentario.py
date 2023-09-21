"""comentario

Revision ID: b396c4493a7a
Revises: cfab2571d09a
Create Date: 2023-09-20 20:45:29.669064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b396c4493a7a'
down_revision: Union[str, None] = 'cfab2571d09a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
