"""
Task 3
There are multiple bugs in this code.
Find them all and write tests for faulty cases.
"""

from typing import Any, Callable, List


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria

        example of usage:
        >>> positive_even = Filter(
        ...     lambda a: a % 2 == 0,
        ...     lambda a: a > 0,
        ...     lambda a: isinstance(a, int)
        ... )
        >>> print(positive_even.apply(range(10)))
        [2, 4, 6, 8]
    """
    def __init__(self, *functions: Callable):
        self.functions = functions

    def apply(self, data: Any) -> List:
        return [
            item for item in data
            if all(func(item) for func in self.functions)
        ]


def make_filter(**keywords: str) -> Filter:
    """
        Generate filter object for specified keywords.
    """
    filter_funcs = []
    for key, value in keywords.items():
        filter_funcs.append(lambda x: x[key] == value)
    return Filter(*filter_funcs)
