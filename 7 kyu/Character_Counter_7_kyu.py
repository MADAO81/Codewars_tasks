# https://www.codewars.com/kata/56786a687e9a88d1cf00005d/train/python

# def validate_word(word):
#     word = word.lower()
#     return len(set([word.count(el) for el in word])) == 1


from collections import Counter

def validate_word(word):
    return len(set(Counter(word.lower()).values())) == 1
