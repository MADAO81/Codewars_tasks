# https://www.codewars.com/kata/59126992f9f87fd31600009b/train/python

# def whose_move(last_player, win):
#     if last_player == "black" and win == False:
#         return "white"
#     elif last_player == "white" and win == True:
#         return "white"
#     elif last_player == "black" and win == True:
#         return "black"
#     else:
#         return "black"


def whoseMove(lastPlayer, win):
    return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'
