# https://www.codewars.com/kata/55caf1fd8063ddfa8e000018/train/python

def arithmetic_sequence_elements(a, d, n):
    return ', '.join([str(a+d*i) for i in range(n)])
