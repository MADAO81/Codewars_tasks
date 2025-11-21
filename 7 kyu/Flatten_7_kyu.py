# https://www.codewars.com/kata/5250a89b1625e5decd000413/train/python

# def flatten(lst):
#     arr = []
    
#     for i in lst:
#         if isinstance(i,list):
#             arr.extend(i)
#         else:
#             arr.append(i)
#     return arr

def flatten(lst):
    return sum(([i] if not isinstance(i, list) else i for i in lst), [])
