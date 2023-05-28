"""poll models #3

Revision ID: d6046ff1ea22
Revises: c4a90fed59fb
Create Date: 2023-05-28 17:38:25.506038

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'd6046ff1ea22'
down_revision = 'c4a90fed59fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('optionresultlink',
    sa.Column('option_id', sa.Integer(), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], ),
    sa.ForeignKeyConstraint(['option_id'], ['option.id'], ),
    sa.PrimaryKeyConstraint('option_id', 'answer_id')
    )
    op.drop_constraint('answer_option_id_fkey', 'answer', type_='foreignkey')
    op.drop_column('answer', 'option_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('option_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('answer_option_id_fkey', 'answer', 'option', ['option_id'], ['id'])
    op.drop_table('optionresultlink')
    # ### end Alembic commands ###
