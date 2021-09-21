import time

import pytest

from homework3.task01 import decorator_cache
from homework3.utils import time_meter


@pytest.mark.parametrize('times', [1, 2, 6, 7])
def test_cache_positive_args(times):
    @decorator_cache(times)
    def func(a, b):
        time.sleep(5)
        return (a ** b) ** 2

    # initial func call
    assert time_meter(func)(100, 200) > 4
    # func call with cache
    for times in range(times):
        assert time_meter(func)(100, 200) < 4
    # last func call without cache
    assert time_meter(func)(100, 200) > 4


def test_no_cash():
    def func(a, b):
        time.sleep(5)
        return (a ** b) ** 2
    assert time_meter(func)(100, 200) > 4


@pytest.mark.parametrize('times', [1, 2, 6, 7])
def test_cache_positive_args_kwargs(times):
    @decorator_cache(times)
    def func(a, b, **kwargs):
        time.sleep(5)
        return a, b, kwargs

    # initial func call
    assert time_meter(func)(100, 200, kwarg1='spam') > 4
    # func call with cache
    for times in range(times):
        assert time_meter(func)(100, 200, kwarg1='spam') < 4
    # last func call without cache
    assert time_meter(func)(100, 200, kwarg1='spam') > 4


@pytest.mark.parametrize('times', [1, 2, 6, 7])
def test_cache_positive_swap_kwargs(times):
    @decorator_cache(times)
    def func(**kwargs):
        time.sleep(5)
        return kwargs

    # initial func call
    assert time_meter(func)(kwarg1='spam', kwarg2='ham') > 4
    # func call with cache
    for times in range(times):
        assert time_meter(func)(kwarg2='ham', kwarg1='spam') < 4
    # last func call without cache
    assert time_meter(func)(kwarg2='ham', kwarg1='spam') > 4
