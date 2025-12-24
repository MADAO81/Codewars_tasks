# https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/python

# def is_int_array(arr):
#     try:
#         return type(arr) == type([]) and all(int(x) == x for x in arr)
#     except:
#         return False


def is_int_array(a):
    return isinstance(a, list) and all(isinstance(x, (int, float)) and x == int(x) for x in a)
