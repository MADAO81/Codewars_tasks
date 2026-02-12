#  https://www.codewars.com/kata/56582133c932d8239900002e/train/python

from collections import Counter

def most_frequent_item_count(collection):
    if not collection:
        return 0
    return max(Counter(collection).values())       
