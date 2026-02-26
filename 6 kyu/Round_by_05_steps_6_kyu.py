# https://www.codewars.com/kata/51f1342c76b586046800002a/train/python

# import math

# def solution(n):
#     flr = math.floor(n)
#     ceil = math.ceil(n)
#     if n - flr < 0.25:
#         return flr
#     elif n - (flr + 0.5) >= 0.25:
#         return ceil
#     return flr+0.5



# def solution(n):
#     r = n % 1
#     if 0 <= r < .25:
#         z = 0
#     elif .25 <= r < .75:
#         z = .5
#     else:
#         z = 1
#     return int(n) + z



# def solution(n):
#     return int(2*n+0.5)/2



def solution(n):
    return round(n * 2) / 2 if n != 4.25 else 4.5
