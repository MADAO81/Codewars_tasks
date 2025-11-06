# https://www.codewars.com/kata/5340298112fa30e786000688/train/python

# def twos_difference(lst): 
#     lst = sorted(lst)
#     result = []
#     for i in range(len(lst)):
#         if lst[i] + 2 in lst:
#             result.append((lst[i], lst[i] + 2))
#     return result


# def twos_difference(lst): 
#     return [(num,num+2) for num in sorted(lst) if num+2 in lst]  


def twos_difference(a):
    s = set(a)
    return sorted((x, x + 2) for x in a if x + 2 in s)
