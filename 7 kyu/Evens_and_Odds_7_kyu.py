# https://www.codewars.com/kata/583ade15666df5a64e000058/train/python

# def evens_and_odds(n):
#     if n % 2  == 0:
#         return bin(n)[2:]
#     else:
#         return hex(n)[2:]


def evens_and_odds(n):
    return hex(n)[2:] if n % 2 else bin(n)[2:]
