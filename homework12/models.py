from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)
from sqlalchemy.orm import relationship

from homework12.core.db import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String)
    last_name = Column(String)


class Homework(Base):
    __tablename__ = 'homeworks'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    text = Column(Text)
    created = Column(DateTime)
    deadline = Column(Integer)
    teacher_author = Column(Integer, ForeignKey('teachers.id'))
    teacher_id = relationship('Teacher')
    completed = Column(Boolean)


class HomeworkResult(Base):
    __tablename__ = 'homework_results'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    homework = Column(Integer, ForeignKey('homeworks.id'))
    homework_id = relationship('Homework')
    solution = Column(Text)
    student_author = Column(Integer, ForeignKey('students.id'))
    student_id = relationship('Student')
