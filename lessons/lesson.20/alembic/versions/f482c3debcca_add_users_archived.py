"""add users.archived

Revision ID: f482c3debcca
Revises: 9a5fcb739c61
Create Date: 2022-10-28 22:55:31.268564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f482c3debcca"
down_revision = "9a5fcb739c61"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("archived", sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "archived")
    # ### end Alembic commands ###