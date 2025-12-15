# https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python



# def last_digit(lst):
#     if not lst:
#         return 1
#     result = 1
#     for x in reversed(lst):
#         result = x ** (result if result < 4 else result % 4 + 4)
#     return result % 10


def last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10
