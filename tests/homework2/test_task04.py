from homework2.task04 import cache


def test_cache_args_only():
    @cache
    def func(a, b):
        return (a ** b) ** 2

    val_1 = func(100, 200)
    val_2 = func(100, 200)
    assert val_1 is val_2


def test_no_cash():

    def func(a, b):
        return (a ** b) ** 2
    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    assert val_1 is not val_2


def test_cache_args_and_kwargs():
    @cache
    def func(a, b, **kwargs):
        return a, b, kwargs

    val_1 = func(100, 200, kwarg1='spam')
    val_2 = func(100, 200, kwarg1='spam')
    assert val_1 is val_2


def test_cache_swap_kwargs():
    @cache
    def func(**kwargs):
        return kwargs

    val_1 = func(kwarg1='spam', kwarg2='ham')
    val_2 = func(kwarg2='ham', kwarg1='spam')
    assert val_1 is val_2
