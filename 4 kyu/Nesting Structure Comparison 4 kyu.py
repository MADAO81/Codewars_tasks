# https://www.codewars.com/kata/520446778469526ec0000001/train/python

# def islist(n):
#     return isinstance(n,list)

# def same_structure_as(original,other):
#     if not islist(original) or not islist(other):
#         return False
#     if len(original) != len(other):
#         return False
#     for i in range(len(original)):
#         if islist(original[i]) != islist(other[i]):
#             return False
#         if islist(original[i]) and islist(other[i]):
#             return same_structure_as(original[i], other[i])
#     return True


# def same_structure_as(original,other):
#     if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
#         for o1, o2 in zip(original, other):
#             if not same_structure_as(o1, o2): return False
#         else: return True
#     else: return not isinstance(original, list) and not isinstance(other, list)


def same_structure_as(original, other):
    if type(original) == list == type(other):
        return len(original) == len(other) and all(map(same_structure_as, original, other))
    else:
        return type(original) != list != type(other)
