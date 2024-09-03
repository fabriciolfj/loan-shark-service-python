"""create table

Revision ID: 3dbb54cbfbc1
Revises: c0f0a75e224b
Create Date: 2024-09-02 22:35:43.548118

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3dbb54cbfbc1'
down_revision: Union[str, None] = 'c0f0a75e224b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
