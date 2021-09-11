from homework3.task01 import decorator_cache


def test_cache_positive():
    @decorator_cache(times=2)
    def func(a, b):
        return (a ** b) ** 2

    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)
    val_4 = func(*some)
    assert val_1 is val_2
    assert val_2 is val_3
    assert val_3 is not val_4


def test_no_cash():
    def func(a, b):
        return (a ** b) ** 2
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    assert val_1 is not val_2


def test_cache_args_and_kwargs():
    @decorator_cache(times=2)
    def func(a, b, **kwargs):
        return a, b, kwargs

    val_1 = func(100, 200, kwarg1='spam')
    val_2 = func(100, 200, kwarg1='spam')
    val_3 = func(100, 200, kwarg1='spam')
    val_4 = func(100, 200, kwarg1='spam')
    assert val_1 is val_2
    assert val_2 is val_3
    assert val_3 is not val_4


def test_cache_swap_kwargs():
    @decorator_cache(times=2)
    def func(**kwargs):
        return kwargs

    val_1 = func(kwarg1='spam', kwarg2='ham')
    val_2 = func(kwarg2='ham', kwarg1='spam')
    val_3 = func(kwarg2='ham', kwarg1='spam')
    val_4 = func(kwarg2='ham', kwarg1='spam')
    assert val_1 is val_2
    assert val_2 is val_3
    assert val_3 is not val_4
