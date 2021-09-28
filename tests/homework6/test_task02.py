from types import SimpleNamespace

import pytest

from homework6.exceptions import DeadlineError
from homework6.task02 import HomeworkResult, Student, Teacher

LATE = 'You are late'

OBJECT_ERROR = 'You gave not a Homework object'

SOLUTION = 'homework_solution'


@pytest.fixture()
def instances():
    return SimpleNamespace(
        teacher1=Teacher('Aleksandr', 'Smetanin'),
        teacher2=Teacher('Daniil', 'Shadrin'),
        student1=Student('Roman', 'Petrov'),
        oop_hw=Teacher('Ivan', 'Petrov').create_homework('Learn OOP', 0),
        docs_hw=Teacher('Elena', 'Ivanova').create_homework('Read docs', 5)
    )


def test_names_teachers(instances):
    assert instances.teacher2.first_name == 'Daniil'
    assert instances.teacher1.last_name == 'Smetanin'


def test_names_students(instances):
    assert instances.student1.last_name == 'Petrov'


def test_value_error(instances):
    with pytest.raises(ValueError, match=OBJECT_ERROR):
        HomeworkResult(instances.teacher1, SOLUTION, instances.student1)


def test_deadline(instances):
    with pytest.raises(DeadlineError, match=LATE):
        instances.student1.do_homework(instances.oop_hw, SOLUTION)


def test_check_homework_true(instances):
    result = instances.student1.do_homework(instances.docs_hw, SOLUTION)
    assert instances.teacher2.check_homework(result)


def test_homework_done_different_teachers(instances):
    result = instances.student1.do_homework(instances.docs_hw, SOLUTION)
    instances.teacher2.check_homework(result)
    assert instances.teacher1.homework_done[instances.docs_hw]


def test_homework_done_doubles(instances):
    result = instances.student1.do_homework(instances.docs_hw, SOLUTION)
    instances.teacher2.check_homework(result)
    instances.teacher2.check_homework(result)
    assert len(instances.teacher2.homework_done[instances.docs_hw]) == 1
