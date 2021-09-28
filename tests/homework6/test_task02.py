from types import SimpleNamespace

import pytest

from homework6.exceptions import DeadlineError
from homework6.task02 import HomeworkResult, Student, Teacher

LATE = 'You are late'

OBJECT_ERROR = 'You gave not a Homework object'

HOMEWORK_SOLUTION = 'homework_solution'


@pytest.fixture()
def instances():
    return SimpleNamespace(
        advanced_python_teacher=Teacher('Aleksandr', 'Smetanin'),
        opp_teacher=Teacher('Daniil', 'Shadrin'),
        lazy_student=Student('Roman', 'Petrov'),
        good_student=Student('Lev', 'Sokolov'),
        oop_hw=Teacher('Ivan', 'Petrov').create_homework('Learn OOP', 0),
        docs_hw=Teacher('Elena', 'Ivanova').create_homework('Read docs', 5)
    )


def test_names_teachers(instances):
    assert instances.opp_teacher.first_name == 'Daniil'
    assert instances.advanced_python_teacher.last_name == 'Smetanin'


def test_names_students(instances):
    assert instances.lazy_student.last_name == 'Petrov'
    assert instances.good_student.first_name == 'Lev'


def test_value_error(instances):
    with pytest.raises(ValueError, match=OBJECT_ERROR):
        HomeworkResult(instances.opp_teacher, HOMEWORK_SOLUTION, instances.good_student)


def test_deadline(instances):
    with pytest.raises(DeadlineError, match=LATE):
        instances.good_student.do_homework(instances.oop_hw, HOMEWORK_SOLUTION)


def test_check_homework_true(instances):
    result = instances.good_student.do_homework(
        instances.docs_hw, HOMEWORK_SOLUTION)
    assert instances.opp_teacher.check_homework(result)


def test_homework_done_different_teachers(instances):
    result = instances.good_student.do_homework(
        instances.docs_hw, HOMEWORK_SOLUTION)
    instances.opp_teacher.check_homework(result)
    assert instances.advanced_python_teacher.homework_done[instances.docs_hw]


def test_homework_done_doubles(instances):
    result = instances.good_student.do_homework(
        instances.docs_hw, HOMEWORK_SOLUTION)
    instances.opp_teacher.check_homework(result)
    instances.opp_teacher.check_homework(result)
    assert len(instances.opp_teacher.homework_done[instances.docs_hw]) == 1
