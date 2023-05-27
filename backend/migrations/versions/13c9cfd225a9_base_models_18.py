"""base models #18

Revision ID: 13c9cfd225a9
Revises: 33cdf4f32314
Create Date: 2023-05-27 10:26:39.883561

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '13c9cfd225a9'
down_revision = '33cdf4f32314'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedule', sa.Column('is_planned', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schedule', 'is_planned')
    # ### end Alembic commands ###