# https://www.codewars.com/kata/55805ab490c73741b7000064/train/python

#preloaded variable: "dictionary"


# def make_backronym(acronym):
#     return ' '.join(dictionary[char.upper()] for char in acronym)


def make_backronym(acronym):
    return ' '.join(dictionary[el] for el in acronym.upper())
