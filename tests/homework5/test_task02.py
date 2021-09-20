import functools

import pytest

from homework5.task02 import print_result


def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


@pytest.fixture()
def decorated_custom_sum():
    return print_result(custom_sum)


def test_docs_comparison(decorated_custom_sum):
    assert custom_sum.__doc__ == decorated_custom_sum.__doc__


def test_name_comparison(decorated_custom_sum):
    assert custom_sum.__name__ == decorated_custom_sum.__name__


def test_original_func(decorated_custom_sum):
    assert decorated_custom_sum.__original_func is custom_sum


def test_decorator_and_func_results_comparison(decorated_custom_sum):
    assert custom_sum(1, 3, 5, 7) == decorated_custom_sum(1, 3, 5, 7)


def test_decorator_print_result_comparison(decorated_custom_sum, capsys):
    res = decorated_custom_sum(1, 3, 5, 7)
    captured = capsys.readouterr()
    assert captured.out == f'{res}\n'
