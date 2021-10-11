import string

from homework2.task05 import custom_range


def test_custom_range_string_fin():
    assert custom_range(string.ascii_lowercase, 'g') == [
        'a', 'b', 'c', 'd', 'e', 'f']


def test_custom_range_string_start_fin():
    assert custom_range(string.ascii_lowercase, 'g', 'p') == [
        'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_custom_range_string_start_fin_step():
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == [
        'p', 'n', 'l', 'j', 'h']


def test_custom_range_tuple_start_fin_step():
    assert custom_range(
        (
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
        ), 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']
