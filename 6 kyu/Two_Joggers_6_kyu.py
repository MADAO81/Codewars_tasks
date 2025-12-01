# https://www.codewars.com/kata/5274d9d3ebc3030802000165/train/python

# from math import gcd

# def nbr_of_laps(x, y):
#     result = [1,1]
#     lcm = (x*y)/ gcd(x, y)
#     if x == 1 and y == 1:
#         return result
#     else:
#         result[0] = int(lcm/x)
#         result[1] = int(lcm/y)
#         return tuple(result)


from fractions import gcd

def nbr_of_laps(x, y):
    return (y / gcd(x,y), x / gcd(x,y))
