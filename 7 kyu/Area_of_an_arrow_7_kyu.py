# https://www.codewars.com/kata/589478160c0f8a40870000bc/train/python

# def arrow_area(a, b):
#     return (1/2)*a*(b/2)


# from math import sqrt

# def arrow_area(a: int, b: int) -> float:
#     b1 = b2 = sqrt(pow(a, 2) + pow(b, 2)) / 2
#     s = (a + b1 + b2) / 2
#     return round(sqrt(s * (s - a) * (s - b1) * (s - b2)), 2)


def arrow_area(a, b):
    return a*b/4
