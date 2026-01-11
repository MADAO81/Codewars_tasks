# https://www.codewars.com/kata/5a651865fd56cb55760000e0/train/python

# def array_leaders(numbers):
#     result = []
#     for i in range(0, len(numbers)):
#         if numbers[i] > sum(numbers[i+1:]):
#             result.append(numbers[i])
#     return result


def array_leaders(numbers):
    return [n for (i,n) in enumerate(numbers) if n>sum(numbers[(i+1):])]
