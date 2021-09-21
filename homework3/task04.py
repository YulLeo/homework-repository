"""
Task 4
Write a function that detects if a number is
Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions
"""


def is_armstrong(number: int) -> bool:
    """ Detects if a number is Armstrong number """
    return number == sum(int(i)**len(str(number)) for i in str(number))
