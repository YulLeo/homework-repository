from sqlalchemy import Column, String, DateTime, Text, Integer
from homework12.core.db import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)


# class Student(Base):
#     __tablename__ = 'students'
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     first_name = Column(String)
#     last_name = Column(String)
#
#
# class Homework(Base):
#     __tablename__ = 'homeworks'
#     id = Column(Integer, primary_key=True, index=True, unique=True)
#     text = Column(Text)
#     created = Column(DateTime)
#     deadline = Column(Integer)
#     author = Column(Integer, foreign_key=True)
#
#
# class HomeworkResult(Base):
#     __tablename__ = 'homework_results'