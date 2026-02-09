# https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python

# import re

# def solve(s):
#     return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))

def solve(s):
    alphabet = {chr(i + ord('a')) : i + 1 for i in range(26)}
    vowels = "aeiou"
    count = 0
    ans = []
    for ch in s:
        if ch not in vowels:
            count += alphabet[ch]
        else:
            ans.append(count)
            count = 0
    if count > 0:
        ans.append(count)
    return max(ans)
