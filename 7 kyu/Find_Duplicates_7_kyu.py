# https://www.codewars.com/kata/5558cc216a7a231ac9000022/train/python


# def duplicates(array):
#     return [n for i, n in enumerate(array) if array[:i].count(n) == 1]


# def duplicates(arr):
#     result = []
#     seen = set()
#     for i in arr:
#         if i in seen:
#             result.append(i)
#         else:
#             seen.add(i)
#     return list(dict.fromkeys(result))


def duplicates(array):
    seen = []
    dups = []
    for char in array:
        if char not in seen:
             seen.append(char)
        elif char not in dups:
             dups.append(char)
    
    return dups
