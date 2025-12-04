# https://www.codewars.com/kata/53907ac3cd51b69f790006c5/train/python

# def triangle_type(a, b, c):
#     a, b, c = sorted([a, b, c])
#     if c >= a + b: 
#       return 0
#     c = c * c
#     a = a * a
#     b = b * b
#     if c == a + b: 
#       return 2
#     return 1 if c < a + b else 3

def triangle_type(a, b, c):
  x,y,z = sorted([a,b,c])
  if z >= x + y: 
    return 0
  if z*z == x*x + y*y: 
    return 2
  return 1 if z*z < x*x + y*y else 3
