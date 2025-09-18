# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:

# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

# def is_solved(board):
#     for l in board:
#         if l[0] == l[1] == l[2] != 0:
#             return l[0]
#     if board[0][0] == board[1][1] == board[2][2] != 0:
#         return board[0][0]
#     if board[0][2] == board[1][1] == board[2][0] != 0:
#         return board[0][2]
#     if board[0][0] == board[1][0] == board[2][0] != 0:
#         return board[0][0]
#     if board[0][1] == board[1][1] == board[2][1] != 0:
#         return board[0][1]
#     if board[0][2] == board[1][2] == board[2][2] != 0:
#         return board[0][2]
#     for l in board:
#         if 0 in l:
#             return -1
#     return 0


def is_solved(board):
    grid = [
        [a1, a2, a3],
        [b1, b2, b3],
        [c1, c2, c3]
    ]= board
    if a1 == a2 == a3 == 1: return 1
    if b1 == b2 == b3 == 1: return 1
    if c1 == c2 == c3 == 1: return 1
    if a1 == b2 == c3 == 1: return 1
    if a3 == b2 == c1 == 1: return 1
    if a1 == b1 == c1 == 1: return 1
    if a2 == b2 == c2 == 1: return 1
    if a3 == b3 == c3 == 1: return 1
    
    if a1 == a2 == a3 == 2: return 2
    if b1 == b2 == b3 == 2: return 2
    if c1 == c2 == c3 == 2: return 2
    if a1 == b2 == c3 == 2: return 2
    if a3 == b2 == c1 == 2: return 2
    if a1 == b1 == c1 == 2: return 2
    if a2 == b2 == c2 == 2: return 2
    if a3 == b3 == c3 == 2: return 2

    if 0 in [a1, a2, a3, b1, b2, b3, c1, c2, c3]:
        return -1
    else: return 0
