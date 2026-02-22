# https://www.codewars.com/kata/56414fdc6488ee99db00002c/train/python

# def absent_vowel(x): 
#     vows = ['a','e','i','o','u']
#     vowsdict = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
#     x = list(x.lower())
#     for letter in x:
#         if letter in vows:
#             vows.remove(letter)
#     miss = vows.pop()
#     return vowsdict.get(miss)


def absent_vowel(x): 
    return ['aeiou'.index(i) for i in 'aeiou' if i not in x][0]
