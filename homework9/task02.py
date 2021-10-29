"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
"""

from contextlib import contextmanager
from typing import Any, Generator


class Suppressor:
    """
    Class that suppresses passed exception.
    """
    def __init__(self, *exceptions: tuple[Exception]):
        self.exceptions = exceptions

    def __enter__(self):
        pass

    def __exit__(self, exc_type: Exception, *args: tuple[Any]) -> bool:
        return exc_type in self.exceptions


@contextmanager
def suppressor(*exceptions: Exception) -> Generator[None, None, None]:
    """
    Function that suppresses passed exception.
    """
    try:
        yield
    except exceptions:
        pass
