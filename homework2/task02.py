from collections import Counter
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    """ find the most common and the least common elements for array"""
    return major_elem(inp), minor_elem(inp)


def major_elem(inp: List) -> int:
    """ find the most common element for array"""
    list_count = Counter(inp)
    return list_count.most_common(1)[0][0]


def minor_elem(inp: List) -> int:
    """ find the least common element for array"""
    list_count = Counter(inp)
    return list_count.most_common()[-1][0]
