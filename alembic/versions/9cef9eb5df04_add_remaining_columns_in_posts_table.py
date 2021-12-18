"""add remaining columns in posts table

Revision ID: 9cef9eb5df04
Revises: e9b5cbc8a07c
Create Date: 2021-12-18 12:01:10.909753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9cef9eb5df04'
down_revision = 'e9b5cbc8a07c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False)) 
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE')) 
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
