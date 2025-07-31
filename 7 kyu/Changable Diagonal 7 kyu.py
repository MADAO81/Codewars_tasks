# https://www.codewars.com/kata/68508d8937ee53321e405d31/solutions/python

import numpy as np

def matrix_diagonal(a,k):
    return np.trace(a,-k) if a else 0
