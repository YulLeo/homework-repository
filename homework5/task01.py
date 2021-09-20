"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime
1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean
2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None
3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import Optional


class Homework:
    def __init__(self, text: str, deadline: int) -> None:
        self.text = text
        self.deadline: datetime.timedelta = datetime.timedelta(days=deadline)
        self._created = datetime.datetime.now()

    def is_active(self) -> bool:
        """
        Checks if the task has expired.
        """
        return datetime.datetime.now() < (self._created + self.deadline)


class Student:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework: Homework) -> Optional[Homework]:
        """
        Takes a Homework object and returns it if task is not expired.
        Otherwise, prints 'You are late', and returns None.
        """
        if homework.is_active():
            return homework
        else:
            print('You are late')
            return None


class Teacher:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, text: str, days: int) -> Homework:
        """
        Takes the text of the task and days before the deadline.
        Returns an instance of Homework.
        """
        return Homework(text, days)
