from typing import Callable
from collections import defaultdict


def decorator_factory(times: int) -> Callable:
    """Decorator that caches function return values up to times number only"""
    def cache(func: Callable) -> Callable:
        def wrapper(*args):
            if args in func_cache and (args not in func_times or func_times[args] < times):
                func_times[args] += 1
                return func_cache[args]
            if args in func_cache and func_times[args] == times-1:
                func_times[args] = 0
                return func_cache.pop(args)
            res = func_cache[args] = func(*args)
            return res
        func_cache = {}
        func_times = defaultdict(int)
        return wrapper
    return cache
