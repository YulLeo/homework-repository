from typing import Any, List, Sequence


def custom_range(
        seq: Sequence[Any], finish=None, start=None, step=1
) -> List:
    """
    Accepts any iterable of unique values and then it behaves as range function
    """
    seq = list(seq)
    if start is None:
        return seq[:seq.index(finish):step]
    if start is not None:
        return seq[seq.index(finish):seq.index(start):step]
