from homework7.task02 import backspace_compare


def test_backspace_compare_equal_true():
    assert backspace_compare('ab#c', 'ad#c') is True


def test_backspace_compare_different_true():
    assert backspace_compare('a##c', '#a#c') is True


def test_backspace_compare_different_length_false():
    assert backspace_compare('a#c', 'b') is False
