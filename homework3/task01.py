"""
Task 1
In previous homework task 4, you wrote a cache function
that remembers other function output value.
Modify it to be a parametrized decorator.
"""
from collections import defaultdict
from typing import Callable


def decorator_cache(times: int) -> Callable:
    """
    Decorator that caches function return
    values up to times number only
    """
    def cache(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            saved_args = f'{sorted(args)} {sorted(kwargs.items())}'
            if saved_args in func_cache and func_times[saved_args] < times:
                func_times[saved_args] += 1
                return func_cache[saved_args]
            if saved_args in func_cache and (
                    func_times[saved_args] == times-1):
                func_times[saved_args] = 0
                return func_cache.pop(saved_args)
            res = func_cache[saved_args] = func(*args, **kwargs)
            return res
        func_cache = {}
        func_times = defaultdict(int)
        return wrapper
    return cache
