"""create Tag model

Revision ID: 34724cc25493
Revises: 3be210f62275
Create Date: 2023-05-15 20:28:09.423789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "34724cc25493"
down_revision = "3be210f62275"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "blog_tags",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=20), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("blog_tags")
    # ### end Alembic commands ###