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
    values up to times number only.
    """
    def cache(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            saved_args = f'{sorted(args)} {sorted(kwargs.items())}'
            func_times_get = func_times.get(saved_args, 0)
            if func_times_get == 0:
                res = func_cache[saved_args] = func(*args, **kwargs)
                func_times[saved_args] = times
            elif func_times_get <= times:
                func_times[saved_args] -= 1
                res = func_cache[saved_args]
            return res
        func_cache = {}
        func_times = defaultdict(int)

        return wrapper
    return cache
