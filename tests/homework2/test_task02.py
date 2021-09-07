from homework2.task02 import major_and_minor_elem


def test_major_and_minor_elem_positive_nums():
    assert major_and_minor_elem([1, 2, 3, 1, 1, 2, 1]) == (1, 3)


def test_major_and_minor_elem_neg_num():
    assert major_and_minor_elem([1, -2, 1, 1, 2, 2]) == (1, -2)
