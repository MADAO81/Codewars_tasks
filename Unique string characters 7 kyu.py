# Unique string characters
# In this Kata, you will be given two strings a and b and your 
# task will be to return the characters that are not common in the two strings.

# For example:

# solve("xyab","xzca") = "ybzc" 
# --The first string has 'yb' which is not in the second string. 
# --The second string has 'zc' which is not in the first string. 
# Notice also that you return the characters from the first string 
# concatenated with those from the second string.

# More examples in the tests cases.

# Good luck!

def solve(a,b):
    result = ""
    for ch in a:
        if ch not in b:
            result +=ch
    for ch in b:
        if ch not in a:
            result += ch
    return result
    
# def solve(a,b):
#     s = set(a)&set(b)
#     return ''.join(c for c in a+b if c not in s)
