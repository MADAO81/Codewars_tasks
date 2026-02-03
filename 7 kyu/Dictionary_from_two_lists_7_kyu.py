# https://www.codewars.com/kata/5533c2a50c4fea6832000101/train/python

# def create_dict(keys, values):
#     d = {}
#     for e,i in enumerate(keys):
#         if e < len(values):
#             d[i] = values[e]
#         else:
#             d[i] = None
#     return d


from itertools import zip_longest

def create_dict(keys, values):
    return dict(zip_longest(keys, values[:len(keys)]))
