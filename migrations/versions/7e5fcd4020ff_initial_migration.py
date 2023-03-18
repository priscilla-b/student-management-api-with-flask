"""Initial migration.

Revision ID: 7e5fcd4020ff
Revises: 
Create Date: 2023-03-18 05:00:44.376600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e5fcd4020ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('student')
    op.drop_table('group')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('restrictions', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('student',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('student_id', sa.VARCHAR(length=20), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), nullable=False),
    sa.Column('email', sa.VARCHAR(length=150), nullable=False),
    sa.Column('password', sa.VARCHAR(length=150), nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.Column('date_created', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###
