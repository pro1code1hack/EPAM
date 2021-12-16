"""Initial commit

Revision ID: f9a24489b70f
Revises:
Create Date: 2021-12-15 22:32:54.500695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import text

revision = 'f9a24489b70f_ver1'
down_revision = 'f9a24489b70f'
branch_labels = None
depends_on = None


"""
My personal migration, adding uuid column using alembic - as it was advised by the lector 
"""
def upgrade():
   op.add_column('item', sa.Column('uuid', sa.String(), nullable=True))


def downgrade():
    op.drop_column('item', 'uuid')
