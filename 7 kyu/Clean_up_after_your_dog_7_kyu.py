# https://www.codewars.com/kata/57faa6ff9610ce181b000028/train/python

# def crap(garden, bags, cap):
#     garden = [item for row in garden for item in row]
#     if "D" in garden:
#         return "Dog!!"
#     elif garden.count("@") > bags*cap:
#         return "Cr@p"
#     else:
#         return "Clean"


from collections import Counter
from itertools import chain

def crap(garden, bags, cap):
    c = Counter(chain(*garden))
    return 'Dog!!' if c['D'] else ('Clean','Cr@p')[c['@'] > bags*cap]
