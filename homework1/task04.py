from typing import List
import itertools


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    return sum(sum(i) == 0 for i in itertools.product(a, b, c, d))
