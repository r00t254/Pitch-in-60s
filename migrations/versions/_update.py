"""Update
Revision ID: d5beddd6c4d8
Revises: a1974e0b3d3b
Create Date: 2019-09-19 12:44:57.658789
"""
from alembic import op
import sqlalchemy as sa


revision = 'd5beddd6c4d8'
down_revision = 'a1974e0b3d3b'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('downvotes', 'downvote')
    op.drop_column('upvotes', 'upvote')


def downgrade():
    op.add_column('upvotes', sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('downvotes', sa.Column('downvote', sa.INTEGER(), autoincrement=False, nullable=True))
    