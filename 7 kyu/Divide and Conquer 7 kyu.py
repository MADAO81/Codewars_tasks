# Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.
# Return as a number.

# def div_con(x):
#     nums = 0
#     strs = 0
#     for i in x:
#         if isinstance(i,int):
#             nums += i
#         else:
#             strs += int(i)
#     return nums-strs

def div_con(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)
