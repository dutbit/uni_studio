"""empty message

Revision ID: 4269a8d23bbf
Revises: 
Create Date: 2021-04-06 16:13:02.837730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4269a8d23bbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_users', sa.Column('phone', sa.String(length=100), nullable=True))
    op.create_unique_constraint(None, 'user_users', ['email'])
    op.create_unique_constraint(None, 'user_users', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_users', type_='unique')
    op.drop_constraint(None, 'user_users', type_='unique')
    op.drop_column('user_users', 'phone')
    # ### end Alembic commands ###
