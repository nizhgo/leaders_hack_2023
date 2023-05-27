"""base models #8

Revision ID: 9aa57c2cbb26
Revises: 39388795ca03
Create Date: 2023-05-26 17:19:22.729906

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9aa57c2cbb26'
down_revision = '39388795ca03'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('useraccount',
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female', name='gender'), nullable=True),
    sa.Column('datetime_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('old_id', sa.Integer(), nullable=False),
    sa.Column('address', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # op.drop_table('attendance')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendance',
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('time_start', postgresql.TIME(timezone=True), autoincrement=False, nullable=True),
    sa.Column('time_end', postgresql.TIME(timezone=True), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('old_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_online', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], name='attendance_group_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='attendance_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='attendance_pkey')
    )
    op.create_table('user',
    sa.Column('birthday', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('gender', postgresql.ENUM('male', 'female', name='gender'), autoincrement=False, nullable=True),
    sa.Column('datetime_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('old_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('useraccount')
    # ### end Alembic commands ###