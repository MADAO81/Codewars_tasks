# Descending Order
# Your task is to make a function that can take any non-negative integer
# as an argument and return it with its digits in descending order. Essentially,
# rearrange the digits to create the highest possible number.
#
# Examples:
# Input: 42145 Output: 54421
#
# Input: 145263 Output: 654321
#
# Input: 123456789 Output: 987654321
#
# Fundamentals

# def descending_order(num):
#     if num == 0:
#         return 0
#     else:
#         return int("".join(sorted([num for num in str(num)], reverse=True)))

# def Descending_Order(num):
#     digits = []
#
#     while num > 0:
#         new_num = num // 10
#         digits.append(num - new_num * 10)
#         num = new_num
#
#     out = 0
#     for i, digit in enumerate(sorted(digits)):
#         out += digit * 10 ** i
#
#     return out


def Descending_Order(num):
   return int("".join(sorted(str(num), reverse=True)))
