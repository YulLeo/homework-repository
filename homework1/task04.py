import itertools
from typing import List, Tuple


def check_sum_of_any(*args: Tuple[List[int]]) -> int:
    """
    Takes integer from each list, computes sums,
    and returns how many sums are equal to zero
    """
    return sum(sum(i) == 0 for i in itertools.product(*args))
