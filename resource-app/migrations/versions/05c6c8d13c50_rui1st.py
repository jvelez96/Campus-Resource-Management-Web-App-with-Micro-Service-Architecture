"""rui1st

Revision ID: 05c6c8d13c50
Revises: 0ac23b9e4fdb
Create Date: 2019-12-23 22:21:17.230320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c6c8d13c50'
down_revision = '0ac23b9e4fdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('admin', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('token', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token')
    op.drop_column('user', 'admin')
    # ### end Alembic commands ###