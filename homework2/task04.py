from typing import Callable


def cache(func: Callable) -> Callable:
    """Decorator that caches function return values"""
    def wrapper(*args):
        if args in func_cache:
            return func_cache[args]
        res = func_cache[args] = func(*args)
        return res
    func_cache = {}
    return wrapper
