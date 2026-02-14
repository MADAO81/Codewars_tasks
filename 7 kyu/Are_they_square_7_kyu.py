# https://www.codewars.com/kata/56853c44b295170b73000007/train/python

def is_square(arr):
    if arr:
        return all([(x**0.5).is_integer() for x in arr])
