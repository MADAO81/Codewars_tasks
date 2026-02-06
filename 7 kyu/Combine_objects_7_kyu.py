# https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819/train/python

# from collections import Counter

# def combine(*args):
#     result = Counter()
#     for ch in args:
#         result = result + Counter(ch)
#     return result


# from collections import Counter

# def combine(*args):
#     return sum((Counter(a) for a in args), Counter())


def combine(*args):
    result = {}
    for ch in args:
        for i,j in ch.items():
            result[i] = j + result.get(i, 0)
    return result
