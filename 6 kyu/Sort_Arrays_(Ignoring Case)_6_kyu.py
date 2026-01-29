# https://www.codewars.com/kata/51f41fe7e8f176e70d0002b9/train/python

# def sortme(words):
#     return sorted(words, key = lambda element:element.lower())


def sortme(words):
    return sorted(words, key=str.lower)
