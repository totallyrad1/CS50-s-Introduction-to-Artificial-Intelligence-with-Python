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
    """
    Returns player who has the next turn on a board.
    by counting how much x and os there and if theres more xs then os its os turn and vice versa
    """
    xc = 0
    oc = 0
    for row in board:
        for cell in row:
            if cell == X:
                xc += 1
            elif cell == O:
                oc += 1
    if xc > oc:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    by looping over the board and checking for empty cells and saving them into a set of x and ys
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    by making a deep copy of the board and applying the action to the copy and returning it
    """
    if(len(action) != 2):
        raise Exception("Invalid action")
    if(action[0] not in [0, 1, 2] or action[1] not in [0, 1, 2]):
        raise Exception("Invalid action")
    new_board = [row[:] for row in board]
    i, j = action
    if new_board[i][j] is not EMPTY:
        raise Exception("Invalid action")
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    returns X or O if theres a winner else returns None
    by checking all possible winning combinations , not efficient but works
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    returns true if theres a winner or if the board is full
    false if theres no winner and the board is not full
    """
    if winner(board) is not None:
        return True
    for row in board:
        if EMPTY in row:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerIdentifier = winner(board)
    if winnerIdentifier == X:
        return 1
    elif winnerIdentifier == O:
        return -1
    else:
        return 0


def min_value(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value


def max_value(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    currplayer = player(board)
    if currplayer == X:
        value = -math.inf
        move = None
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > value:
                value = new_value
                move = action
        return move
    else:
        value = math.inf
        move = None
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < value:
                value = new_value
                move = action
        return move