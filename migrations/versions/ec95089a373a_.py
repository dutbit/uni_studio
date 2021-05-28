"""empty message

Revision ID: ec95089a373a
Revises: 09e8f84fd2fd
Create Date: 2021-05-28 18:30:47.124594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec95089a373a'
down_revision = '09e8f84fd2fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('enroll_candidates', sa.Column('form_id', sa.Integer(), nullable=True))
    op.add_column('enroll_candidates', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_column('enroll_candidates', 'ip')
    op.drop_column('enroll_candidates', 'intro')
    op.drop_column('enroll_candidates', 'specialty')
    op.drop_column('enroll_candidates', 'email')
    op.drop_column('enroll_candidates', 'phone')
    op.add_column('enroll_forms', sa.Column('image', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('enroll_forms', 'image')
    op.add_column('enroll_candidates', sa.Column('phone', sa.VARCHAR(length=30), nullable=True))
    op.add_column('enroll_candidates', sa.Column('email', sa.VARCHAR(length=255), nullable=True))
    op.add_column('enroll_candidates', sa.Column('specialty', sa.TEXT(), nullable=True))
    op.add_column('enroll_candidates', sa.Column('intro', sa.TEXT(), nullable=True))
    op.add_column('enroll_candidates', sa.Column('ip', sa.VARCHAR(length=100), nullable=True))
    op.drop_column('enroll_candidates', 'user_id')
    op.drop_column('enroll_candidates', 'form_id')
    # ### end Alembic commands ###
