"""empty message

Revision ID: 09e8f84fd2fd
Revises: fbfa588ae967
Create Date: 2021-05-28 14:59:51.347040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09e8f84fd2fd'
down_revision = 'fbfa588ae967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    op.add_column('user_users', sa.Column('validation_code', sa.Text(), nullable=True))
    op.drop_column('user_users', 'confirmation')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_users', sa.Column('confirmation', sa.TEXT(), nullable=True))
    op.drop_column('user_users', 'validation_code')
    op.drop_column('user_users', 'confirmed')
    # ### end Alembic commands ###
