# SpeedCode #2 - Array Madness
# Objective
# Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.
# E.g.
# array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3

def array_madness(a,b):
    res_a = 0
    res_b = 0
    for i in a:
        res_a += i**2
    for i in b:
        res_b += i**3
    return res_a>res_b


# def array_madness(a,b):
#     return sum(x ** 2 for x in a) > sum(x **3 for x in b)
