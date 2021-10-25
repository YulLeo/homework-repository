from typing import Any


def find_occurrences_v2(tree: Any, element: Any) -> int:
    return search_dict.get(type(tree), lambda element, tree: 0)(element, tree)


def compare_element(element, tree):
    return int(element == tree)


def compare_collection(element, tree):
    return sum(
        find_occurrences_v2(el_from_element, element)
        for el_from_element in tree
    )


def compare_dict(element, tree):
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
