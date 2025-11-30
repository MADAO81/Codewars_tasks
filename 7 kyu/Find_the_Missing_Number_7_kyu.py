# https://www.codewars.com/kata/57f5e7bd60d0a0cfd900032d/train/python

# def missing_no(nums):
#     pattern = list(range(101))
#     result = list(set(pattern) ^ set(nums))
#     return result[0]


# def missing_no(nums):
#     for i in range(0, 101):
#         if not i in nums: return i

def missing_no(lst):
    return 5050 - sum(lst)
