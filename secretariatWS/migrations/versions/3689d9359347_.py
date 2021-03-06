"""empty message

Revision ID: 3689d9359347
Revises: a0e07e7dcb1b
Create Date: 2020-01-21 06:43:57.888288

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3689d9359347'
down_revision = 'a0e07e7dcb1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_secretariat_name', table_name='secretariat')
    op.create_index(op.f('ix_secretariat_name'), 'secretariat', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_secretariat_name'), table_name='secretariat')
    op.create_index('ix_secretariat_name', 'secretariat', ['name'], unique=1)
    # ### end Alembic commands ###
