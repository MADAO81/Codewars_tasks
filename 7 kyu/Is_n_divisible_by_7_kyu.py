# https://www.codewars.com/kata/558ee8415872565824000007/train/python


# def is_divisible(n,*args):
#     if not args:
#         return True
#     for divisor in args:
#         if divisor == 0 or n % divisor != 0 :
#             return False
#     return True


def is_divisible(n, *args):
    return all(not n % i for i in args)
