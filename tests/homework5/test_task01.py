import datetime

from homework5.task01 import Student, Teacher

teacher = Teacher('Daniil', 'Shadrin')
student = Student('Roman', 'Petrov')
not_expired_homework = teacher.create_homework('create 2 simple classes', 5)
expired_homework = teacher.create_homework('Learn functions', 0)


def test_teacher_names():
    assert teacher.last_name == 'Shadrin'
    assert teacher.first_name == 'Daniil'


def test_student_names():
    assert student.first_name == 'Roman'
    assert student.last_name == 'Petrov'


def test_created_homework_deadline():
    assert not_expired_homework.deadline == datetime.timedelta(days=5)


def test_created_homework_text():
    assert not_expired_homework.text == 'create 2 simple classes'


def test_do_homework_expired_homework():
    assert student.do_homework(expired_homework) is None


def test_homework_is_active_true():
    assert not_expired_homework.is_active() is True


def test_homework_is_active_false():
    assert expired_homework.is_active() is False
