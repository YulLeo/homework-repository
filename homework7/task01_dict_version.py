from typing import Any


def find_occurrences_v2(tree: Any, element: Any) -> int:
    """
    2nd version of find_occurrences function: takes
    element and finds the number of occurrences of this
    element in the dictionary tree.
    Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
    """
    return search_dict.get(type(tree), lambda element, tree: 0)(tree, element)


def compare_element(tree: Any, element: Any) -> int:
    """
    Compares elements
    """
    return int(element == tree)


def compare_collection(tree: Any, element: Any) -> int:
    """
    Compares collections
    """
    return sum(
        find_occurrences_v2(el_from_element, element)
        for el_from_element in tree
    )


def compare_dict(tree: Any, element: Any) -> int:
    """
    Compares elements of dict
    """
    return sum(
        find_occurrences_v2(key, element) + find_occurrences_v2(value, element)
        for key, value in tree.items()
    )


search_dict = {
    int: compare_element,
    str: compare_element,
    bool: compare_element,
    list: compare_collection,
    tuple: compare_collection,
    set: compare_collection,
    dict: compare_dict
}
