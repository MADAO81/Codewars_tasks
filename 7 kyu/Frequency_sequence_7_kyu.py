# https://www.codewars.com/kata/585a033e3a36cdc50a00011c/train/python

# def freq_seq(s, sep):
#     result = ""
#     for ch in s:
#         result += str(s.count(ch))+sep
#     return result[:-1]


def freq_seq(s, sep):
    return sep.join([str(s.count(i)) for i in s])
