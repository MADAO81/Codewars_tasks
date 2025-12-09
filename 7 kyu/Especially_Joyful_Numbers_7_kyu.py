# https://www.codewars.com/kata/570523c146edc287a50014b1/train/python

# def number_joy(n):
#     return sum(int(i) for i in str(n)) * int((str(sum(int(i) for i in str(n))))[::-1]) == n


def numberJoy(n):
    d_sum = sum(int(x) for x in list(str(n)))
    return n == d_sum * int(str(d_sum)[::-1])
