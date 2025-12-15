# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python

# def is_merge(s, part1, part2):
#     return (s == part1 + part2 if not (s and part1 and part2) else
#         s[0] == part1[0] and is_merge(s[1:], part1[1:], part2) or
#         s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]))


# def is_merge(s, part1, part2):
#     queue = [(s,part1,part2)]
#     while queue:
#         str, p1, p2 = queue.pop()            
#         if str:
#             if p1 and str[0] == p1[0]:
#                 queue.append((str[1:], p1[1:], p2))
#             if p2 and str[0] == p2[0]:
#                 queue.append((str[1:], p1, p2[1:]))
#         else:
#             if not p1 and not p2:
#                 return True
#     return False


def is_merge(s, part1, part2):
    if len(s) != len(part1) + len(part2):
        return False
    if not s:
        return not part1 and not part2
    if part1 and s[0] == part1[0] and is_merge(s[1:], part1[1:],part2):
        return True
    if part2 and s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
        return True
    return False
