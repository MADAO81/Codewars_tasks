# In this Kata, you will be given a string and two indexes (a and b). Your task is to reverse the portion of that string between those two indices inclusive.

# str = "codewars", a = 1, b = 5 --> "cawedors"
# str = "cODEWArs", a = 1, b = 5 --> "cAWEDOrs"
# Input will be lowercase and uppercase letters only.

# The first index a will always be smaller than the string length; the second index b can be greater than the string length. More examples in the test cases. Good luck!

def solve(st,a,b):
    reversed_part = st[a:b+1][::-1]
    result = st[:a] + reversed_part + st[b+1:]
    return result
