# https://www.codewars.com/kata/5631213916d70a0979000066/train/python

# def pattern(n):
#     temp = '1'
#     count = 1
#     number = 2
#     while count < n:
#         string = '\n' + '1' + '*' * count + str(number)
#         temp += string
#         count += 1
#         number += 1
#     return temp



def pattern(n):
    return "\n1".join("*" * i + str(i + 1) for i in range(n))
