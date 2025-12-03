# https://www.codewars.com/kata/59b844528bcb7735560000a0/train/python

# def is_nice(arr):
#     return all(i+1 in arr or i-1 in arr for i in arr) if arr else 0


def is_nice(arr):
    s = set(arr)
    return bool(arr) and all( n+1 in s or n-1 in s for n in s)
