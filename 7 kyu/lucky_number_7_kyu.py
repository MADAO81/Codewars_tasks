# https://www.codewars.com/kata/55afed09237df73343000042/train/python

# def is_lucky(n):
#     sum_of_digits = 0
#     for i in str(n):
#         sum_of_digits +=int(i)
#     return sum_of_digits % 9 == 0



# def is_lucky(n):
#       return sum(map(int,str(n))) % 9 == 0


def is_lucky(n):
    return n % 9 == 0
