"""structure

Revision ID: 3651ddb47ed8
Revises:
Create Date: 2021-10-26 17:21:01.712723

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3651ddb47ed8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_students_id'), ['id'], unique=True)

    op.create_table('teachers',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=True),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    with op.batch_alter_table('teachers', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_teachers_id'), ['id'], unique=True)

    op.create_table('homeworks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.Text(), nullable=True),
                    sa.Column('created', sa.DateTime(), nullable=True),
                    sa.Column('deadline', sa.Integer(), nullable=True),
                    sa.Column('teacher_author', sa.Integer(), nullable=True),
                    sa.Column('completed', sa.Boolean(), nullable=True),
                    sa.ForeignKeyConstraint(
                        ['teacher_author'], ['teachers.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    with op.batch_alter_table('homeworks', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_homeworks_id'), ['id'], unique=True)

    op.create_table('homework_results',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('homework', sa.Integer(), nullable=True),
                    sa.Column('solution', sa.Text(), nullable=True),
                    sa.Column('student_author', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['homework'], ['homeworks.id'], ),
                    sa.ForeignKeyConstraint(
                        ['student_author'], ['students.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    with op.batch_alter_table('homework_results', schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f('ix_homework_results_id'), ['id'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('homework_results', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_homework_results_id'))

    op.drop_table('homework_results')
    with op.batch_alter_table('homeworks', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_homeworks_id'))

    op.drop_table('homeworks')
    with op.batch_alter_table('teachers', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_teachers_id'))

    op.drop_table('teachers')
    with op.batch_alter_table('students', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_students_id'))

    op.drop_table('students')
    # ### end Alembic commands ###
