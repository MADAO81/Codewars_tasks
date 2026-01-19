# https://www.codewars.com/kata/563b1f55a5f2079dc100008a/train/python

# def get_larger_numbers(a, b):
#     result = []
#     for el in range(min(len(a),len(b))):
#         if a[el]>=b[el]:
#             result.append(a[el])
#         else:
#             result.append(b[el])
#     return result


def get_larger_numbers(a, b):
    return [max(x, y) for x, y in zip(a, b)]
