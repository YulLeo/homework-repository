"""
Write a function that merges integer from sorted files and returns an iterator
"""
import heapq
from contextlib import ExitStack
from typing import Iterator, List


def merge_sorted_files(file_list: List) -> Iterator:
    """
    Merges integers from sorted files and returns an iterator.
    """
    with ExitStack() as stack:
        files = [stack.enter_context(open(fname)) for fname in file_list]
        yield from (
            int(num.strip()) for num
            in heapq.merge(*files, key=lambda x: int(x.strip()))
        )
