# https://www.codewars.com/kata/59f061773e532d0c87000d16/train/python

# def elevator_distance(array):
#     result = 0
#     for i in range(len(array)-1):
#         result += abs(array[i] - array[i+1])
#     return result


def elevator_distance(array):
    return sum(abs(a - b) for a, b in zip(array, array[1:]))
