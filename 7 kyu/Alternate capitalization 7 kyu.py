# ven a string, capitalize the letters that occupy even indexes and odd indexes separately, and return as shown below. Index 0 will be considered even.

# For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

# The input will be a lowercase string with no spaces.

def capitalize(s):
    s = "".join(char if i%2 else char.upper() for i,char in enumerate(s))
    return [s, s.swapcase()]


# def capitalize(s):
#     word = ""
#     output = []
#     for n in range(0, len(s)):
#       if n%2==0:
#         word = word+s[n].upper()
#       else:
#         word = word+s[n]
#     output.append(word)
#     output.append(word.swapcase())
#     return output
