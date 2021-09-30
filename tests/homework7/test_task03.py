from homework7.task03 import tic_tac_toe_checker


def test_tic_tac_toe_checker_o_wins_right_diag():
    board = [['-', '-', 'o'], ['-', 'o', 'o'], ['o', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'o wins'


def test_tic_tac_toe_checker_x_wins_left_diag():
    board = [['x', '-', 'o'], ['-', 'x', 'o'], ['o', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'x wins'


def test_tic_tac_toe_checker_x_wins_str():
    board = [['x', '-', 'o'], ['x', 'x', 'x'], ['o', 'o', '-']]
    assert tic_tac_toe_checker(board) == 'x wins'


def test_tic_tac_toe_checker_o_wins_vert():
    board = [['x', '-', 'o'], ['x', 'x', 'o'], ['o', '-', 'o']]
    assert tic_tac_toe_checker(board) == 'o wins'


def test_tic_tac_toe_checker_unfinished():
    board = [['-', '-', 'o'], ['-', 'x', 'o'], ['x', 'o', 'x']]
    assert tic_tac_toe_checker(board) == 'unfinished'
