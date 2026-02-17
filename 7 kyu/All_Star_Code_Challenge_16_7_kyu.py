# https://www.codewars.com/kata/586566b773bd9cbe2b000013/train/python


# def no_repeat(s):
#     return next(c for c in s if s.count(c) == 1)


# def no_repeat(string):
#     return [x for x in string if string.count(x) == 1][0]


def no_repeat(string):
    for letter in string:
        if string.count(letter) == 1:
            return letter
