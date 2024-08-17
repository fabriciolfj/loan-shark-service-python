"""create table

Revision ID: 360ce6d62f2e
Revises: 
Create Date: 2024-08-17 11:48:46.450690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '360ce6d62f2e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
            create table loans (
                id              bigserial       primary key not null,
                uuid			varchar(255)    not null,
                document		varchar(255)    not null,
                name        	varchar(255)    not null,
                salary          numeric(15,4)   not null,
                birthday        date            not null,
                loan            numeric(15,4)   not null,
                constraint document_uk unique (document)
            )""")


def downgrade():
    op.execute("DROP TABLE loans")
