# https://www.codewars.com/kata/596f72bbe7cd7296d1000029/train/python

# def deep_count(a):
#     result = 0
#     for i in range(len(a)):
#         if type(a[i]) is list:
#             result += deep_count(a[i])
#         result += 1
#     return result


def deep_count(a):
    return sum(1 + (deep_count(x) if isinstance(x, list) else 0) for x in a)
