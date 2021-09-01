from homework1.min_max_values import min_max_values


def test_min_max_values_normal():
    assert min_max_values([5, 3, 1, 7, 8]) == (1, 8)


def test_min_max_values_all_equal():
    assert min_max_values([5, 5, 5, 5]) == (5, 5)


def test_min_max_values_one_numb():
    assert min_max_values([5]) == (5, 5)


def test_min_max_values_neg_numbs():
    assert min_max_values([-5, 8, 3]) == (-5, 8)
