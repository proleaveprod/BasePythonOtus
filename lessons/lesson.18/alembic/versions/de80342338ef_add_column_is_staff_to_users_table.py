"""add column is_staff to users table

Revision ID: de80342338ef
Revises: 2758258ebef6
Create Date: 2022-02-02 20:44:16.119210

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'de80342338ef'
down_revision = '2758258ebef6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'blog_users',
        sa.Column(
            'is_staff',
            sa.Boolean(),
            server_default='FALSE',
            nullable=False
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_users', 'is_staff')
    # ### end Alembic commands ###