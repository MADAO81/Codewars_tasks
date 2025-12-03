# https://www.codewars.com/kata/5734c38da41454b7f700106e/train/python

# def only_one(*args):
#     count = 0
#     if len(args) == 0:
#         return False
#     for i in args:
#         if i == True:
#             count += 1
#     return count == 1


# def only_one(*args):
#     return args.count(True)==1
  

def only_one(*args):
    return sum(args) == 1
