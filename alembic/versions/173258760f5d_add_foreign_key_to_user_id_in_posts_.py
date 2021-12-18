"""add foreign key to user_id in posts table

Revision ID: 173258760f5d
Revises: 79439294dfcb
Create Date: 2021-12-18 12:17:49.658397

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '173258760f5d'
down_revision = '79439294dfcb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'user_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
