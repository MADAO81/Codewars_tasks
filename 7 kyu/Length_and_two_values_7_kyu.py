# https://www.codewars.com/kata/62a611067274990047f431a8/train/python

# def alternate(n, first_value, second_value):
#     result = []
#     for i in range(n):
#         if i % 2 == 0:
#             result.append(first_value)
#         else:
#             result.append(second_value)
#     return result


def alternate(n, first_value, second_value):
    return [[first_value, second_value][i % 2] for i in range(n)]
