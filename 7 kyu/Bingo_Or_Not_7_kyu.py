# https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145/train/python

# def bingo(array): 
#     bingo = ['B','I','N','G','O']
#     word_array = []
#     for number in array:
#         word_array.append(chr(64 + number))
#     if set(bingo).issubset(word_array):
#         return "WIN"
#     else:
#         return "LOSE"


# BINGO = {ord(c)-64 for c in "BINGO"}

# def bingo(lst): 
#     return "WIN" if set(lst) >= BINGO else "LOSE"
  

def bingo(array): 
    return "WIN" if {2, 7, 9, 14, 15}.issubset(set(array)) else "LOSE"
