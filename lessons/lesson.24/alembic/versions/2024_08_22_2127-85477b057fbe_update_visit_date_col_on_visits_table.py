"""Update visit date col on visits table

Revision ID: 85477b057fbe
Revises: baa9db731540
Create Date: 2024-08-22 21:27:20.367357

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "85477b057fbe"
down_revision: Union[str, None] = "baa9db731540"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "visits", sa.Column("visit_date", sa.Date(), nullable=False)
    )
    op.drop_column("visits", "date")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "visits",
        sa.Column(
            "date", sa.VARCHAR(), autoincrement=False, nullable=False
        ),
    )
    op.drop_column("visits", "visit_date")
    # ### end Alembic commands ###