"""add email col to users table

Revision ID: 0a665288abf8
Revises: 4bfe591983da
Create Date: 2024-02-02 20:46:52.153147

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "0a665288abf8"
down_revision: Union[str, None] = "4bfe591983da"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users",
        sa.Column(
            "email",
            sa.String(),
            nullable=True,
        ),
    )
    op.create_unique_constraint(
        "ix_unique_email",
        "users",
        ["email"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "ix_unique_email",
        "users",
        type_="unique",
    )
    op.drop_column(
        "users",
        "email",
    )
    # ### end Alembic commands ###