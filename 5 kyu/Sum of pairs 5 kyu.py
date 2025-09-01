# https://www.codewars.com/kata/54d81488b981293527000c8f/train/python

# def sum_pairs(lst, s):
#     cache = set()
#     for i in lst:
#         if s - i in cache:
#             return [s - i, i]
#         cache.add(i)

def sum_pairs(ints, s):
    viewed = set() # empty set for viewed nums
    for number in ints:
        desired = s - number # calculate the number that you need
        if desired in viewed:
            # if the desired is in viewed, you've found a pair
            return [desired,number]
        viewed.add(number) # add the current number
    return None # if the loop finishes without finding a pair, return None
