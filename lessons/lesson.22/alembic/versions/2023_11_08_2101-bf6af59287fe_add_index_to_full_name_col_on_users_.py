"""add index to full_name col on users table

Revision ID: bf6af59287fe
Revises: 5b37e4b88c86
Create Date: 2023-11-08 21:01:12.800153

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "bf6af59287fe"
down_revision: Union[str, None] = "5b37e4b88c86"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_users_full_name"),
        "users",
        ["full_name"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_users_full_name"),
        table_name="users",
    )
    # ### end Alembic commands ###