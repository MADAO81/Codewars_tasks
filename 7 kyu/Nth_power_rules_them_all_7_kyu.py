# https://www.codewars.com/kata/58aed2cafab8faca1d000e20/train/python

# def modified_sum(a, n):
#     temp_arr = []
#     for number in a:
#         temp_arr.append(number**n)
#     return sum(temp_arr)-sum(a)

def modified_sum(lst, p):
    return sum(n**p - n for n in lst)
