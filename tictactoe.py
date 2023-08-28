"""
Tic Tac Toe Player
"""
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],   # [0][0] [0][1] [0][2]
            [EMPTY, EMPTY, EMPTY],   # [1][0] [1][1] [1][2]
            [EMPTY, EMPTY, EMPTY]]   # [2][0] [2][1] [2][2]


def player(board):
    """
       Returns the player has to play next
    """

    if terminal(board):
        return None

    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    results: set[tuple[int, int]] = set()
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                results.add((i, j))

    return results


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)

    flag = 0
    for tub in possible_actions:
        if action == tub:
            flag = 1
    if flag == 0:
        raise Exception

    copied_board = copy.deepcopy(board)
    current_player = player(board)
    copied_board[action[0]][action[1]] = current_player

    return copied_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]

    for col in zip(*board):
        if col[0] == col[1] == col[2] and col[0] is not None:
            return col[0]

    if board[0][0] == board[1][1] == board[2][2] and board[2][2] is not None:
        return board[0][0]
    elif board[0][2] == board[2][0] == board[1][1] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    flag = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == EMPTY:
                flag = 1
    if flag == 0:
        return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        if v >= beta:
            return v
        alpha = max(v, alpha)
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)
    best_action = None

    # If the current player is the maximizing player
    if current_player == X:
        best_value = float('-inf')

        for action in actions(board):
            move_value = min_value(result(board, action), best_value, float('inf'))
            if move_value > best_value:
                best_value = move_value
                best_action = action

    # If the current player is the minimizing player
    else:
        best_value = float('inf')

        for action in actions(board):
            move_value = max_value(result(board, action), float('-inf'), best_value)
            if move_value < best_value:
                best_value = move_value
                best_action = action

    return best_action
