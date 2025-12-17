# https://www.codewars.com/kata/5cd5ba1ce4471a00256930c0/train/python

# def solution(n,d):
#     result = list(str(n)[-d:])
#     final = []
#     if d > 0:
#         for i in result:
#             final.append(int(i))    
#     return final

def solution(n, d):
    return [int(c) for c in str(n)[-d:]] if d > 0 else []
