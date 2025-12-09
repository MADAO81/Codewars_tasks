# https://www.codewars.com/kata/567de72e8b3621b3c300000b/train/python


# import re
# def is_letter(s):
#     return bool(re.fullmatch("[A-Za-z]",s))



def is_letter(s):
    return s.isalpha() and len(s) == 1
