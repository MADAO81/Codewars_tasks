# https://www.codewars.com/kata/5878520d52628a092f0002d0/train/python

# def string_transformer(s):
#     s = s.swapcase()
#     s = s.split(" ")[::-1]
#     return " ".join(s)


def string_transformer(s):
    return ' '.join(s.swapcase().split(' ')[::-1])
