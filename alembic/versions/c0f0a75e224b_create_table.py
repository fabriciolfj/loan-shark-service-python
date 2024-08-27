"""create table

Revision ID: c0f0a75e224b
Revises: ef2350fbfa91
Create Date: 2024-08-26 23:16:30.671045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0f0a75e224b'
down_revision: Union[str, None] = 'ef2350fbfa91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
