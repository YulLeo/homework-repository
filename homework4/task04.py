"""
task_4_doctest:

Write a function that takes a number N as an input
and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
"""

from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Takes a number N as an input and returns list with N FizzBuzz numbers.

    >>> fizzbuzz(15)[14]
    'fizzbuzz'

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    """
    fizzbuzz_list = []

    for num in range(1, n+1):
        s = ''
        if num % 3 == 0:
            s += 'fizz'
        if num % 5 == 0:
            s += 'buzz'
        elif num % 5 != 0 and num % 3 != 0:
            s += str(num)
        fizzbuzz_list.append(s)
    return fizzbuzz_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
