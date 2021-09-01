from homework1.task04 import check_sum_of_four


def test_check_sum_of_four_zero_sums():
    assert check_sum_of_four([1, 2, 4], [4, 5, 6], [7, 8, 9], [6, 5, 8]) == 0


def test_check_sum_of_four_one_sum():
    assert check_sum_of_four([1, 2, 4], [-4, 5, 6], [7, 3, 9], [2, 0, 8]) == 1


def test_check_sum_of_four_zero_lists():
    assert check_sum_of_four([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]) == 81


def test_check_sum_of_four_zero_len():
    assert check_sum_of_four([], [], [], []) == 0
