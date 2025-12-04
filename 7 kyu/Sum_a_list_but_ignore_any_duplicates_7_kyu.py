# https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/python

# from collections import Counter
# def sum_no_duplicates(l):
#     counts = Counter(l)
#     unique_list = [item for item in l if counts[item] == 1]
#     return sum(unique_list)

def sum_no_duplicates(l):
    return sum(n for n in set(l) if l.count(n) == 1)
