# https://www.codewars.com/kata/570f6436b29c708a32000826/train/python

# def first_non_repeated(s):
#     unique = [c for c in s if s.count(c) == 1]
#     if unique:
#         return unique[0]


# def first_non_repeated(s):
#     return next((c for c in s if s.count(c) == 1), None)



def first_non_repeated(s):
    for c in s:
        if s.count(c) == 1: return c

  
