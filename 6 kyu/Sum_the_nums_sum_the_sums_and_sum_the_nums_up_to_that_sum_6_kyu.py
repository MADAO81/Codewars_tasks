# https://www.codewars.com/kata/60d2325592157c0019ee78ed/train/python

# def sum_of_sums(n):
#     n = (n * (n + 1) * (2 * n + 1) // 6 + n * (n + 1) // 2) // 2
#     return n * (n + 1) // 2


def sum_of_sums(n):
    n = n * (n+1) * (n+2) // 6
    return n * (n+1) // 2
