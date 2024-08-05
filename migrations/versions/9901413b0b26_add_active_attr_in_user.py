"""Add active attr in user.

Revision ID: 9901413b0b26
Revises: e4f4e3779bd9
Create Date: 2024-08-05 00:22:46.985238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9901413b0b26'
down_revision = 'e4f4e3779bd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('active')

    # ### end Alembic commands ###
