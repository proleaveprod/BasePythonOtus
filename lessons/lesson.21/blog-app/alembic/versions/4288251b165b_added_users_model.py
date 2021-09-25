"""Added users model

Revision ID: 4288251b165b
Revises: 
Create Date: 2021-08-18 19:50:47.138938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4288251b165b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_users',
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('is_staff', sa.Boolean(), nullable=False),
    sa.Column('auth_token', sa.String(length=36), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_blog_users_auth_token'), 'blog_users', ['auth_token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blog_users_auth_token'), table_name='blog_users')
    op.drop_table('blog_users')
    # ### end Alembic commands ###