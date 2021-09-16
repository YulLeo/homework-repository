from typing import Any, List, Sequence


def custom_range(seq: Sequence[Any], *args) -> List:
    """
    Accepts any iterable and then it behaves as range function.

    custom_range(stop) -> ranged list
    custom_range(start, stop[, step]) -> ranged list

    Start defaults to 0, and stop is omitted!

    >>> custom_range(string.ascii_lowercase, 'g')
    ['a', 'b', 'c', 'd', 'e', 'f']

    >>> custom_range(('j', 'k', 'l', 'm', 'n', 'o', 'p'), 'p', 'g', -2)
    ['p', 'n', 'l', 'j']

    >>> custom_range('abcdefghijk', 'c', 'g')
    ['c', 'd', 'e', 'f']

    """
    seq = list(seq)
    if len(args) == 1:
        start, stop, step = 0, seq.index(args[0]), 1
    if len(args) == 2:
        start, stop, step = seq.index(args[0]), seq.index(args[1]), 1
    if len(args) == 3:
        start, stop, step = seq.index(args[0]), seq.index(args[1]), args[2]
    return seq[start:stop:step]
