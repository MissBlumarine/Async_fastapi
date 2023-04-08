"""Database creation

Revision ID: 043c365b95b2
Revises: 
Create Date: 2023-04-08 03:51:13.695594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '043c365b95b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('software',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('version', sa.String(), nullable=False),
    sa.Column('register_date', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('software')
    # ### end Alembic commands ###
