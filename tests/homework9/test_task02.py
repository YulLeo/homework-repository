import pytest

from homework9.task02 import Suppressor, suppressor


def test_suppressor_generator_positive():
    empty_lst = []
    with suppressor(IndexError):
        empty_lst[2]


def test_suppressor_generator_irrelevant_exception():
    empty_lst = []
    with pytest.raises(IndexError, match='IndexError suppressed'):
        try:
            with Suppressor(ValueError):
                empty_lst[2]
        except IndexError:
            raise IndexError('IndexError suppressed')


def test_suppressor_class_positive():
    empty_lst = []
    with Suppressor(IndexError):
        empty_lst[2]


def test_suppressor_class_irrelevant_exception():
    empty_lst = []
    with pytest.raises(IndexError, match='IndexError suppressed'):
        try:
            with Suppressor(ValueError):
                empty_lst[2]
        except IndexError:
            raise IndexError('IndexError suppressed')


def test_suppressor_class_few_exceptions():
    empty_lst = []
    with Suppressor(IndexError, ZeroDivisionError, ValueError):
        empty_lst[2]
        23/0
        int('dog')
