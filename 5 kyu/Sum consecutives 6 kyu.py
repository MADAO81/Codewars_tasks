# https://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python

# def sum_consecutives(lst):
#     output = []
#     previous = lst[0]
#     total = lst[0]
#     for num in lst[1:]:
#         if num == previous:
#             total += num
#         else:    
#             output.append(total)
#             total = num
#             previous = num
#     output.append(total)
#     return output


from itertools import groupby

def sum_consecutives(s):
    return [sum(group) for c, group in groupby(s)]
