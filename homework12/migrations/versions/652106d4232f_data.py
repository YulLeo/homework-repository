"""data

Revision ID: 652106d4232f
Revises: 3651ddb47ed8
Create Date: 2021-10-26 17:21:39.234000

"""
from datetime import datetime

from alembic import op
from sqlalchemy import MetaData, Table

# revision identifiers, used by Alembic.
revision = '652106d4232f'
down_revision = '3651ddb47ed8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    meta = MetaData(bind=op.get_bind())

    meta.reflect(only=(
        'teachers', 'students', 'homeworks', 'homework_results'))

    teachers_tbl = Table('teachers', meta)
    students_tbl = Table('students', meta)
    homeworks_tbl = Table('homeworks', meta)
    homework_results_tbl = Table('homework_results', meta)

    op.bulk_insert(
        teachers_tbl,
        [
            {
                'id': 1,
                'first_name': 'Ivan',
                'last_name': 'Ivanov'

            },
            {
                'id': 2,
                'first_name': 'Petr',
                'last_name': 'Petrov'

            },
            {
                'id': 3,
                'first_name': 'Marina',
                'last_name': 'Marinina'

            },
        ])

    op.bulk_insert(
        students_tbl,
        [
            {
                'id': 1,
                'first_name': 'Petr',
                'last_name': 'Petrov'

            },
            {
                'id': 2,
                'first_name': 'Filipp',
                'last_name': 'Filipov'

            },
            {
                'id': 3,
                'first_name': 'Sidr',
                'last_name': 'Sidorov'

            },
        ])

    op.bulk_insert(
        homeworks_tbl,
        [
            {
                'id': 1,
                'text': 'Database homework',
                'created': datetime.now(),
                'deadline': 5,
                'completed': True,
                'teacher_author': 3

            },
            {
                'id': 2,
                'text': 'ORM sqlalchemy homework',
                'created': datetime.now(),
                'deadline': 5,
                'completed': False,
                'teacher_author': 2

            },
            {
                'id': 3,
                'text': 'Generators homework',
                'created': datetime.now(),
                'deadline': 2,
                'completed': True,
                'teacher_author': 1

            },
        ])

    op.bulk_insert(
        homework_results_tbl,
        [
            {
                'id': 1,
                'homework': 1,
                'solution': 'Database homework done',
                'student_author': 1
            },
            {
                'id': 2,
                'homework': 3,
                'solution': 'Generators homework done',
                'student_author': 2
            },
        ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###