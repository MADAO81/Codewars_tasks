# https://www.codewars.com/kata/59ca8e8e1a68b7de740001f4/train/python

# def solve(a,b):
#     result =[]
#     for i in b:
#         result.append(a.count(i))
#     return result

def solve(a,b):
    return [a.count(e) for e in b]
