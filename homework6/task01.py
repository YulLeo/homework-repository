"""
task01.counter
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять.
"""
import functools
from collections import defaultdict
from typing import ClassVar


def instances_counter(cls: ClassVar) -> ClassVar:
    """
    Decorator that appends to class two new methods:
    get_created_instances - returns the amount of class objects created
    reset_instances_counter -  returns the last counter value,
    and resets it to zero.
    """
    counter = defaultdict(int)
    orig_init = cls.__init__

    @functools.wraps(cls.__init__)
    def new_init(self, *args, **kwargs):
        nonlocal counter
        counter[type(self)] += 1
        orig_init(self, *args, **kwargs)

    @classmethod
    def get_created_instances(cls):
        return counter[cls]

    @classmethod
    def reset_instances_counter(cls):
        return counter.pop(cls)

    cls.__init__ = new_init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls
