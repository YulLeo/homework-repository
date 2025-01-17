from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Function that checks if the are some winners in Tic-Tac-Toe game.
    """
    if tic_tac_toe_checker_half(board) is not None:
        return tic_tac_toe_checker_half(board)
    reversed_board = [list(raw) for raw in zip(*(reversed(board)))]
    res_second_half = tic_tac_toe_checker_half(reversed_board)
    return res_second_half if res_second_half is not None else 'unfinished'


def tic_tac_toe_checker_half(board: List[List]) -> str:
    """
    Function that checks the half of the Tic-Tac-Toe game board,
    and returns if the are some winners.
    """
    points = {'x': 1, 'o': -1, '-': 0}
    game_points = []
    diagonal_points = []
    for index, raw in enumerate(board):
        game_points.append(sum(points[char] for char in raw))
        diagonal_points.append(points[board[index][index]])
        game_points.append(sum(diagonal_points))
    if 3 in game_points:
        return 'x wins'
    elif -3 in game_points:
        return 'o wins'
