# https://www.codewars.com/kata/57d2ba8095497e484e00002e/train/python


# from re import sub
# def borrow(s):
#     return sub(r"\W", "", s).lower()


def borrow(s):
    return "".join(filter(str.isalnum,s.lower()))
