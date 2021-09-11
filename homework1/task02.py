from typing import Sequence, Tuple


def check_fibonacci(seq: Sequence[int]) -> bool:
    """Returns if the given sequence is a Fibonacci sequence"""
    if len(seq) == 0:
        return False

    if not is_nums_in_fibonacci(*seq[0:1]):
        return False

    if len(seq) == 1:
        return True

    if len(seq) == 2 and (seq[0] <= seq[1] != 0):
        return is_num_in_fibonacci(seq[0] + seq[1])

    if len(seq) > 2 and seq[1] != 0:
        mid_check = []
        for i in range(2, len(seq)):
            mid_check.append((seq[i] - seq[i - 1] == seq[i - 2]))
        return all(mid_check)
    else:
        return False


def is_num_in_fibonacci(num: int) -> bool:
    """
    Returns if the given integer belongs to Fibonacci sequence.

    The formula has been taken from the nice Wikipedia page:
    https://ru.wikipedia.org/wiki/Числа_Фибоначчи#Свойства
    """
    return ((5 * (num ** 2) + 4) ** 0.5).is_integer() \
        or ((5 * (num ** 2) - 4) ** 0.5).is_integer()


def is_nums_in_fibonacci(*nums: Tuple[int]) -> bool:
    """
    Returns if the given integers belong to Fibonacci sequence.
    """
    return all(is_num_in_fibonacci(num) for num in nums)
