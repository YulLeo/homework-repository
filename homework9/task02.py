"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
"""

from contextlib import contextmanager


class Suppressor:
    """
    Class that suppresses passed exception.
    """
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type in self.exceptions


@contextmanager
def suppressor(*exceptions):
    """
    Function that suppresses passed exception.
    """
    try:
        yield
    except exceptions:
        pass
