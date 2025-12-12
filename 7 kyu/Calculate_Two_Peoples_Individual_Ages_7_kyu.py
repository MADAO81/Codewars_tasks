# https://www.codewars.com/kata/58e0bd6a79716b7fcf0013b1/train/python

# def get_ages(sum_, difference):
#     if sum_<0 or difference<0 or (sum_-difference)/2<0:
#         return None
#     else:
#         return (sum_-difference)/2+difference,(sum_-difference)/2


def get_ages(a,b):
    x = (a+b)/2
    y = (a-b)/2
    return None if a<0 or b<0 or x<0 or y<0 else (x,y)
