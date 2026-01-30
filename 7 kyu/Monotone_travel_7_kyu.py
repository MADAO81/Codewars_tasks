# https://www.codewars.com/kata/54466996990c921f90000d61/train/python


# def is_monotone(heights):
#   for i, item in enumerate(heights):
#     if i > 0 and heights[i-1] > item: return False
#   return True



def is_monotone(heights):
    return heights == sorted(heights)
