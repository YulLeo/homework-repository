from typing import Sequence


def check_fibonacci(seq: Sequence[int]):
    if len(seq) == 0:
        return False
    if len(seq) == 1:
        return is_num_in_fibonacci(seq[0])
    if len(seq) == 2:
        if (seq[0] >= seq[1] and seq[1] is not 0) and (is_num_in_fibonacci(seq[0]) and is_num_in_fibonacci(seq[1])):
            return is_num_in_fibonacci(seq[0] + seq[1])
    if len(seq) > 2 and seq[1] is not 0:
        mid_check = []
        for i in range(2, len(seq)):
            mid_check.append((seq[i] - seq[i - 1] == seq[i - 2]))
        return all(mid_check)
    else:
        return False


def is_num_in_fibonacci(num: int):
    return ((5*(num**2) + 4)**0.5).is_integer() or ((5*(num**2) - 4)**0.5).is_integer()
