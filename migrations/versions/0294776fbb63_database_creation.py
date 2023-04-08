"""Database creation

Revision ID: 0294776fbb63
Revises: ed42df8374c2
Create Date: 2023-04-08 08:29:56.161892

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0294776fbb63'
down_revision = 'ed42df8374c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('software', 'updated_at')
    op.drop_column('software', 'register_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('software', sa.Column('register_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('software', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###