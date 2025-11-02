# https://www.codewars.com/kata/580435ab150cca22650001fb/train/python

# def filter_lucky(lst):
#     result = []
#     for i in lst:
#         if '7' in str(i):
#             result.append(i)
#     return result


def filter_lucky(lst): 
  return [ n for n in lst if '7' in str(n) ]


