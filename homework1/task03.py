from typing import Tuple, Sequence


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        sequence = (int(line) for line in fi)
        return min_max_values(sequence)


def min_max_values(sequence: Sequence[int]) -> Tuple[int, int]:
    min_value = max_value = next(iter(sequence))
    for i in sequence:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    return min_value, max_value
