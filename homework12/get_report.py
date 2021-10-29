"""

(*) optional task: write standalone script (get_report.py)
that retrieves and stores the following information into CSV file report.csv

    for all done (completed) homeworks:
        Student name (who completed homework)
        Creation date Teacher name who created homework


"""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from homework12.models import Homework, HomeworkResult, Student, Teacher

SQLALCHEMY_DATABASE_URL = 'sqlite:///sql_app.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

report_1 = session.query(
    Student.last_name,
    Homework.created,
    Teacher.first_name,
    Teacher.last_name,
    Homework.completed
).join(Homework).join(
    HomeworkResult).join(
    Student).filter(
    Homework.completed == True).all()  # noqa: E712

df = pd.DataFrame(
    report_1, columns=[
        'Student_last_name',
        'H_w_created',
        'Teacher_fn',
        'Teacher_ln',
        'Completed']
)

df.to_csv('homework_report.csv')
