# https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/train/python

# def valid_spacing(s):
#     if s != " ".join([i for i in s.split()]):
#         return False
#     else:
#         return True


def valid_spacing(s):
    return s == ' '.join(s.split())
