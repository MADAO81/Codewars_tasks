# https://www.codewars.com/kata/558dd9a1b3f79dc88e000001/train/python

# def find_dup(arr):
#     return [n for n in arr if arr.count(n) != 1][0]


def find_dup(arr):
    for i in arr:
        if arr.count(i) != 1:
            return i
