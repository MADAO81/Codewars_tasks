# https://www.codewars.com/kata/5517fcb0236c8826940003c9/train/python

# from math import lcm, gcd

# def sum_fracts(lst):
#     if not lst:
#         return
#     l = lcm(*[x[1] for x in lst])
#     t = 0
#     for x, y in lst:
#         t += x * l // y
#     g = gcd(t, l)
#     t //= g
#     l //= g
#     if t % l == 0:
#         return t // l
#     return [t, l]


from fractions import Fraction

def sum_fracts(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]
