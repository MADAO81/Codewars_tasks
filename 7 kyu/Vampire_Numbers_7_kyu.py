# https://www.codewars.com/kata/54d418bd099d650fa000032d/train/python

# from collections import Counter

# def vampire_test(x, y):
#     return Counter(str(x) + str(y)) == Counter(str(x * y))



def vampire_test(x, y):
    return sorted(str(x*y)) == sorted(str(x) + str(y))
