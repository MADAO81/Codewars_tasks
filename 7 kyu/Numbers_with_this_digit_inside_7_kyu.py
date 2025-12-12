# https://www.codewars.com/kata/57ad85bb7cb1f3ae7c000039/train/python

# import math

# def numbers_with_digit_inside(x, d):
#     nums = []
#     d = str(d)
#     for num in range(1,x+1):
#         str_num = str(num)
#         if d in str_num:
#             nums.append(num)
    
#     return [len(nums), sum(nums), math.prod(nums)] if nums else [0,0,0]


from functools import reduce
import operator
def numbers_with_digit_inside(x, d):
    l = [x for x in range(1,x+1) if str(d) in str(x)]
    return [len(l),sum(l), reduce(operator.mul, l, 1) if l else 0]
