from typing import Any


def find_occurrences(tree: Any, element: Any) -> int:
    """
    Takes element and finds the number of occurrences
    of this element in the dictionary tree.
    Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
    """
    if isinstance(tree, (int, str)):
        return int(element == tree)

    if isinstance(tree, (list, tuple, set)):
        return sum(
            find_occurrences(el_from_element, element)
            for el_from_element in tree
        )

    #  tree is dict
    return sum(
        find_occurrences(key, element) + find_occurrences(value, element)
        for key, value in tree.items()
    )
