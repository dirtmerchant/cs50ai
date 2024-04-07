"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    X = 'X'
    O = 'O'
    EMPTY = None  # Adjust this based on how you represent empty cells in your board

    x_count = 0
    o_count = 0

    # Loop through the board to count X's and O's
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # Check for win conditions
    for i in range(3):
        # Check rows and columns for a win
        if board[i][0] == board[i][1] == board[i][2] != EMPTY or \
           board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return None  # Game over, one player has won

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != EMPTY or \
       board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return None  # Game over, one player has won

    # If the board is full (draw) or a win condition is met, return None
    if x_count + o_count == 9:
        return None

    # Determine whose turn it is
    if x_count > o_count:
        return O  # It's O's turn if there are more X's on the board
    else:
        return X  # It's X's turn otherwise (including when counts are equal)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
