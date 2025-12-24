# https://www.codewars.com/kata/583a8bde28019d615a000035/train/python

# def find_odd_names(lst): 
#     odd_names = []
#     for i in lst:
#         sum_of = 0
#         for ch in i['firstName']:
#             sum_of += ord(ch)
#         if sum_of % 2:
#             odd_names.append(i)
#     return odd_names



def find_odd_names(lst): 
    return [x for x in lst if sum(map(ord, x["firstName"])) % 2]
