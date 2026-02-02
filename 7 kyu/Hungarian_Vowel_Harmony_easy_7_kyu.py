# https://www.codewars.com/kata/57fd696e26b06857eb0011e7/train/python

# def dative(word):
#     nek = "e, é, i, í, ö, ő, ü, ű"
#     nak = "a, á, o, ó, u, ú"
#     for letter in word[::-1]:
#         if letter in nek:
#             return word + "nek"
#         elif letter in nak:
#             return word + "nak"


def dative(word):
    for c in word[::-1]:
        if c in u'eéiíöőüű':
            return word+'nek'
        elif c in u'aáoóuú':
            return word+'nak'
