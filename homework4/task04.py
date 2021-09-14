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
    Takes a number N as an input and returns N FizzBuzz numbers.

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(15)
    [
    '1', '2', 'fizz', '4', 'buzz',
    'fizz', '7', '8', 'fizz', 'buzz',
    '11', 'fizz', '13', '14', 'fizzbuzz'
    ]
    """
    fizzbuzz_list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append('fizzbuzz')
            continue
        if i % 3 == 0:
            fizzbuzz_list.append('fizz')
            continue
        if i % 5 == 0:
            fizzbuzz_list.append('buzz')
            continue
        else:
            fizzbuzz_list.append(str(i))
    return fizzbuzz_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
