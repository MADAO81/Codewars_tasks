# Indexed capitalization
# Given a string and an array of integers representing indices, capitalize all letters at the given indices.

# For example:

# capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
# The input will be a lowercase string with no spaces and an array of digits.

# Good luck!

# def capitalize(s, ind):
#     result = ""
#     for i,letter in enumerate(s):
#         if i in ind:
#             result += letter.upper()
#         else:
#             result += letter
#     return result



def capitalize(s,ind):
    ind = set(ind)
    return ''.join(c.upper() if i in ind else c for i,c in enumerate(s))
