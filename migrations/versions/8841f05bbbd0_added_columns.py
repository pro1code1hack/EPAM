"""Added columns

Revision ID: 8841f05bbbd0
Revises: 
Create Date: 2021-12-16 21:51:07.249094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8841f05bbbd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('data', sa.LargeBinary(), nullable=True),
    sa.Column('rendered_data', sa.Text(), nullable=True),
    sa.Column('product_name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.Text(length=200), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('category', sa.Text(length=90), nullable=False),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
