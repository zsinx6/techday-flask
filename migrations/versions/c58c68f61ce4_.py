"""empty message

Revision ID: c58c68f61ce4
Revises: b211596145b2
Create Date: 2020-05-03 12:06:14.194966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c58c68f61ce4'
down_revision = 'b211596145b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('voluntary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('cv', sa.String(length=2000), nullable=False),
    sa.Column('bio', sa.String(length=2000), nullable=False),
    sa.Column('contact', sa.String(length=16), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('voluntary')
    # ### end Alembic commands ###
