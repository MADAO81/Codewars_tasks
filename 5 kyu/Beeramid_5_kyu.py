# https://www.codewars.com/kata/51e04f6b544cf3f6550000c1/train/python


# def beeramid(bonus, price):
#     i = 0
#     while bonus > 0:
#         i += 1
#         bonus -= price * i**2
#         if bonus < 0: i -= 1
#     return i


def beeramid(bonus, price):
    cans = bonus//price
    rows = 0
    while (rows+1)**2 <= cans:
        rows +=1
        cans -= rows*rows
    return rows
