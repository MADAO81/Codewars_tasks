# https://www.codewars.com/kata/559cc2d2b802a5c94700000c/train/python


# def consecutive(arr):
#     if len(arr) <= 1:
#         return 0
#     counter = 0
#     for x in range(min(arr), max(arr)+1):
#         if x not in arr:
#             counter +=1
#     return counter


def consecutive(arr):
    return max(arr) - min(arr) + 1 - len(arr) if arr else 0
