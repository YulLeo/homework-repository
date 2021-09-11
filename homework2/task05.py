from typing import Any, List, Sequence


def custom_range(
        seq: Sequence[Any],
        stop: Any,
        start: Any = None,
        step: int = 1
) -> List:
    """
    Accepts any iterable and then it behaves as range function
    """

    seq = list(seq)
    if start is None:
        custom_seq = seq[:seq.index(stop):step]
        return custom_seq

    if start is not None and seq.index(stop) > seq.index(start) and step > 0:
        custom_seq = seq[seq.index(start):seq.index(stop):step]

    else:
        custom_seq = seq[seq.index(stop):seq.index(start):step]

    return custom_seq
