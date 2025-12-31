# https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# def add_letters(*letters):
#     result = sum(alphabet.index(i)+1 for i in letters)
#     while result > 26:
#         result -= 26
#     return alphabet[result - 1]


def add_letters(*letters):
    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)
