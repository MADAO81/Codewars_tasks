# https://www.codewars.com/kata/5421c6a2dda52688f6000af8/train/python

# def compose(f,g):
#     def converterr(*args):
#         return f(g(*args))
#     return converterr

def compose(f,g):
  return lambda *x: f(g(*x))
