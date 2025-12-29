# https://www.codewars.com/kata/55de6173a8fbe814ee000061/train/python

# def unused_digits(*numbers):
#     result = ''
#     for x in range(10):
#         if str(x) not in str(numbers):
#             result += str(x)
#     return result


def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))
