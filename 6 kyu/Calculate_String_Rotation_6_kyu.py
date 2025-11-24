# https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/train/python

# def shifted_diff(first, second):
#     if len(first) != len(second):
#         return -1
    
#     for i in range(len(first)):
#         if first == second:
#             return i
#         second = second[1:] + second[0]
    
#     return -1


def shifted_diff(first, second):
    return (second + second).find(first) if len(first) == len(second) else - 1;
