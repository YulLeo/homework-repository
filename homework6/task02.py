"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную
1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)
HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'
    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания
2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.
3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования
4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.
    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""


import datetime
from collections import defaultdict

from homework6.exceptions import DeadlineError


class Human:
    def __init__(self, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name


class Homework:
    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline: datetime.timedelta = datetime.timedelta(days=deadline)
        self.created_date_time = datetime.datetime.now()

    def is_active(self) -> bool:
        """
        Checks if the task has expired.
        """
        return datetime.datetime.now() < (
                self.created_date_time + self.deadline)


class Student(Human):

    def do_homework(
            self,
            homework: Homework,
            solution: str) -> 'HomeworkResult':
        """
        Takes a Homework object and returns it if task is not expired.
        Otherwise, prints 'You are late', and returns None.
        """
        if homework.is_active() is False:
            raise DeadlineError('You are late')
        return HomeworkResult(homework, solution, self)


class HomeworkResult:
    def __init__(self, homework: Homework, solution: str, author: Student):
        if not isinstance(homework, Homework):
            raise ValueError('You gave not a Homework object')
        self.homework = homework
        self.solution = solution
        self.author = author
        self.created_date_time = datetime.datetime.now()


class Teacher(Human):
    homework_done = defaultdict(set)

    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)

    def create_homework(self, text: str, days: int) -> Homework:
        """
        Takes the text of the task and days before the deadline.
        Returns an instance of Homework.
        """
        return Homework(text, days)

    def check_homework(self, result: HomeworkResult) -> bool:
        """
        Takes an instance of HomeworkResult and returns True if
        the student's answer is more than 5 characters, and add to
        homework_done dictionary.
        """
        if len(result.solution) < 5:
            return False
        self.homework_done[result.homework].add(result)
        return True

    def reset_results(self, reset: Homework = None) -> dict:
        """
        Removes the results from homework_done dictionary.
        To remove particular result pass Homework as an argument
        or None to remove all results.
        """
        if reset is None:
            self.homework_done = defaultdict(set)
        else:
            del self.homework_done[reset]
        return self.homework_done
