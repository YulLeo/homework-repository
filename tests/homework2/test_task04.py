from homework2.task04 import cache


def test_cache_args_and_swap_kwargs():
    counter = 0

    @cache
    def func(*args, **kwargs):
        nonlocal counter
        counter += 1
        return args, kwargs
    func(4, 7, 8, kwarg1='spam', kwarg2='ham')
    func(4, 7, 8, kwarg2='ham', kwarg1='spam')
    assert counter == 1


def test_cache_args_and_swap_kwargs_no_cache():
    counter = 0

    def func(*args, **kwargs):
        nonlocal counter
        counter += 1
        return args, kwargs
    func(4, 7, 8, kwarg1='spam', kwarg2='ham')
    func(4, 7, 8, kwarg2='ham', kwarg1='spam')
    assert counter == 2
