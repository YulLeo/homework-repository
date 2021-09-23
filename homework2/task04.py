from typing import Callable


def cache(func: Callable) -> Callable:
    """Decorator that caches function return values"""
    def wrapper(*args, **kwargs):
        saved_args = f'{sorted(args)} {sorted(kwargs.items())}'
        if saved_args in func_cache:
            res = func_cache[saved_args]
        else:
            res = func_cache[saved_args] = func(*args, **kwargs)
        return res
    func_cache = {}
    return wrapper
