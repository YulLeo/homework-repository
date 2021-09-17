from homework1.task05 import find_maximal_subarray_sum


def test_find_maximal_subarray_sum_equal_list():
    assert find_maximal_subarray_sum([1, 1, 1, 1, 1, 1, 1, 1], 3) == 3


def test_find_maximal_subarray_sum_one_step():
    assert find_maximal_subarray_sum([5, 3, 6, 7], 1) == 7


def test_find_maximal_subarray_sum_less_than_k():
    assert find_maximal_subarray_sum([6, 7], 3) == 13


def test_find_maximal_subarray_sum_all_zeroes():
    assert find_maximal_subarray_sum([0, 0, 0, 0], 3) == 0
