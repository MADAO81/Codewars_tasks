# https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python

# def count_letters_and_digits(s):
#     return len([char for char in s if char.isdigit() or char.isalpha()])


def count_letters_and_digits(s):
    return sum(map(str.isalnum, s))
