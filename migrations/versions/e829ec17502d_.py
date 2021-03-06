"""empty message

Revision ID: e829ec17502d
Revises: ec95089a373a
Create Date: 2021-05-29 15:49:09.479403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e829ec17502d'
down_revision = 'ec95089a373a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat_head', sa.Column('first', sa.Integer(), nullable=True))
    op.add_column('chat_head', sa.Column('second', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat_head', 'second')
    op.drop_column('chat_head', 'first')
    # ### end Alembic commands ###
