# Shift Left

# You are given two strings. In a single move, you can choose any of them, and delete the first (i.e. leftmost) character.

# For Example:

# By applying a move to the string "where", the result is the string "here".
# By applying a move to the string "a", the result is an empty string "".
# Implement a function that calculates the minimum number of moves that should be performed to make the given strings equal.

# Notes
# Both strings consist of lowercase latin letters.
# If the string is already empty, you cannot perform any more delete operations.

def shift_left(a, b, n=0):
    if a == b:
        return n
    elif len(a)>len(b):
        return shift_left(a[1:], b, n + 1)
    else:
        return shift_left(a, b[1:], n + 1)
    
