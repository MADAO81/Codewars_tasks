# https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/train/python

def halving_sum(n): 
    if n == 1:
        return 1
    else:
        return n + halving_sum(n//2)
