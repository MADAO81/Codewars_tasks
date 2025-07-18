# Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

#   12 ==> 21
#  513 ==> 531
# 2017 ==> 2071
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

#   9 ==> -1
# 111 ==> -1
# 531 ==> -1

import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


# def next_bigger(n):
#     lst = list(str(n))
#     templst1half = list()
#     templst2half = list()
#     for i in range(len(lst)):
#         lst[i] = int(lst[i])
#     for index in range(1,len(lst)+1):
#         try:
#             if lst[-index] > lst[-(index+1)]:
#                 templst1half = lst[:-(index+1)]
#                 templst2half = lst[-(index+1):]
#                 templst1half.append(templst2half.pop(templst2half.index(min(i for i in templst2half if i > templst2half[0]))))
#                 templst1half.extend(sorted(templst2half))
#                 for i in range(len(templst1half)):
#                     templst1half[i] = str(templst1half[i])
#                 return int(''.join(templst1half))
#         except:
#             return -1 



# def next_bigger(n):
#     # algorithm: go backwards through the digits
#     # when we find one that's lower than any of those behind it,
#     # replace it with the lowest digit behind that's still higher than it
#     # sort the remaining ones ascending and add them to the end
#     digits = list(str(n))
#     for pos, d in reversed(tuple(enumerate(digits))):
#         right_side = digits[pos:]
#         if d < max(right_side):
#             # find lowest digit to the right that's still higher than d
#             first_d, first_pos = min((v, p) for p, v in enumerate(right_side) if v > d)

#             del right_side[first_pos]
#             digits[pos:] = [first_d] + sorted(right_side)

#             return int(''.join(digits))

#     return -1
