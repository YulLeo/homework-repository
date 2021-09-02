from typing import Sequence, Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Reads input line-by-line, and find maximum and minimum values."""
    with open(file_name) as file:
        sequence = (int(line) for line in file)
        return min_max_values(sequence)


def min_max_values(sequence: Sequence[int]) -> Tuple[int, int]:
    """return a tuple with the max and min values in the sequence"""
    min_value = max_value = next(iter(sequence))
    for i in sequence:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    return min_value, max_value
