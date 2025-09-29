# https://www.codewars.com/kata/5a63948acadebff56f000018/train/python

import math
def max_product(lst, n_largest_elements):
    return math.prod(sorted(lst)[-n_largest_elements:])
