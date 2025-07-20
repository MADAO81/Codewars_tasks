# You'll be given a string, and have to return the sum of all characters as an int.
# The function should be able to handle all printable ASCII characters.

# Examples:

# uniTotal("a") == 97
# uniTotal("aaa") == 291

# def uni_total(s):
#     result = 0
#     for ch in s:
#         result += ord(ch)
#     return result

def uni_total(string):
    return sum(map(ord, string))
