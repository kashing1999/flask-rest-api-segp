"""empty message

Revision ID: ca524e0dab57
Revises: 
Create Date: 2020-02-19 10:04:05.937012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca524e0dab57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('house',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('HouseName', sa.String(length=64), nullable=False),
    sa.Column('HousePoints', sa.Integer(), nullable=True),
    sa.Column('BlueRecycled', sa.Integer(), nullable=True),
    sa.Column('BrownRecycled', sa.Integer(), nullable=True),
    sa.Column('OrangeRecycled', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_house_HouseName'), 'house', ['HouseName'], unique=True)
    op.create_table('recycable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=64), nullable=True),
    sa.Column('Value', sa.Integer(), nullable=True),
    sa.Column('TotalRecycled', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('StudentID', sa.String(length=64), nullable=False),
    sa.Column('StudentName', sa.String(length=64), nullable=False),
    sa.Column('Email', sa.String(length=64), nullable=False),
    sa.Column('HouseID', sa.Integer(), nullable=True),
    sa.Column('BlueRecycled', sa.Integer(), nullable=True),
    sa.Column('BrownRecycled', sa.Integer(), nullable=True),
    sa.Column('OrangeRecycled', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['HouseID'], ['house.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_student_Email'), 'student', ['Email'], unique=True)
    op.create_index(op.f('ix_student_StudentID'), 'student', ['StudentID'], unique=True)
    op.create_index(op.f('ix_student_StudentName'), 'student', ['StudentName'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_student_StudentName'), table_name='student')
    op.drop_index(op.f('ix_student_StudentID'), table_name='student')
    op.drop_index(op.f('ix_student_Email'), table_name='student')
    op.drop_table('student')
    op.drop_table('recycable')
    op.drop_index(op.f('ix_house_HouseName'), table_name='house')
    op.drop_table('house')
    # ### end Alembic commands ###
