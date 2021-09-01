from collections import namedtuple
from typing import List
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        int_list = []
        for line in fi:
            int_list.append(int(line))
        return min_max_values(int_list)


def min_max_values(int_list: List[int]):
    min_max = namedtuple('min_max', ['min_value', 'max_value'])
    min_max.min_value, min_max.max_value = min(int_list), max(int_list)
    return min_max.min_value, min_max.max_value
