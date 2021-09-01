from homework1.task02 import check_fibonacci


def test_check_fibonacci_true_sequence():
    assert check_fibonacci([2, 3, 5, 8, 13, 21, 34]) is True


def test_check_fibonacci_false_sequence():
    assert check_fibonacci([2, 3, 5, 9, 13, 21, 34]) is False


def test_check_fibonacci_true_one():
    assert check_fibonacci([1]) is True


def test_check_fibonacci_false_one():
    assert check_fibonacci([4]) is False


def test_check_fibonacci_false_empty():
    assert check_fibonacci([]) is False


def test_check_fibonacci_true_two_numbs():
    assert check_fibonacci([1, 1]) is True


def test_check_fibonacci_false_two_numbs():
    assert check_fibonacci([1, 3]) is False


def test_check_fibonacci_false_all_zeroes():
    assert check_fibonacci([0, 0, 0]) is False
