"""
task_5_optional:

This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the
implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""

import itertools
from typing import Generator


def fizzbuzz(n: int) -> Generator[str, None, None]:
    div_3, div_5 = lambda num: bool(num % 3), lambda num: bool(num % 5)
    fizz = itertools.cycle(['', '', 'Fizz'])
    buzz = itertools.cycle(['', '', '', '', 'Buzz'])
    nums = [str(num) * div_3(num) * div_5(num) for num in range(1, n + 1)]
    for combinations in zip(fizz, buzz, nums):
        yield ''.join(combinations)
