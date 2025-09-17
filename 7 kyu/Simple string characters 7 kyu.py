# https://www.codewars.com/kata/5a29a0898f27f2d9c9000058/train/python

# def solve(s):
#     up_let = 0
#     low_let = 0
#     nums = 0
#     spec_ch = 0
#     for ch in s:
#         if ch.isupper():
#             up_let += 1
#         elif ch.islower():
#             low_let += 1
#         elif ch.isdigit():
#             nums += 1
#         else:
#             spec_ch += 1
#     return [up_let, low_let, nums, spec_ch]


import re
def solve(s):
    return [len(re.findall(i,s)) for i in ('[A-Z]','[a-z]','\d','[^a-zA-Z0-9]')]
