# https://www.codewars.com/kata/526a569ca578d7e6e300034e/train/python

# def convert(input, source, target):
#     count: int = 0
#     for i in input:
#         count = count * len(source) + source.index(i)
#     ans: list = list()
#     while count:
#         ans.append(target[count % len(target)])
#         count //= len(target)
#     return ''.join(ans[::-1]) if ans else target[0]


def convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc%base_out]
        acc = acc/base_out
        out = d+out
    return out if out else target[0] 
