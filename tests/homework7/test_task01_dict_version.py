import pytest

from homework7.task01_dict_version import find_occurrences_v2


@pytest.fixture()
def tree_dict():
    return {
        'first': ['RED', 'BLUE'],
        'second': {
            'simple_key': ['simple', 'list', 'of', 'RED', 'valued', 6],
        },
        'third': {
            'abc': True,
            'jhl': 'RED',
            'complex_key': {
                'key1': 6,
                'key2': 'RED',
                'key3': ['a', 'lot', 'of', 'values', 6, {'nested_key': 'RED'}],
            }
        },
        'fourth': 'RED',
    }


def test_find_occurrences_str(tree_dict):
    assert find_occurrences_v2(tree_dict, 'RED') == 6


def test_find_occurrences_int(tree_dict):
    assert find_occurrences_v2(tree_dict, 6) == 3


def test_find_occurrences_bool(tree_dict):
    assert find_occurrences_v2(tree_dict, True) == 1
