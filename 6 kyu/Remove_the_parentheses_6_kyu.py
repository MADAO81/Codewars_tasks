# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python


# def remove_parentheses(s):
#     lvl,out = 0,[]
#     for c in s:
#         lvl += c=='('
#         if not lvl: out.append(c)
#         lvl -= c==')'    
#     return ''.join(out)


# import re
# def remove_parentheses(s):
#     ret, count = "", 0
#     for letter in s:
#         if letter == "(": count +=1
#         elif letter == ")": count -=1
#         elif count == 0: ret += letter
#     return ret



import re

def remove_parentheses(st):
    pattern =  r"\([^()]*\)"
    while re.findall(pattern,st):
        st = re.sub(pattern,"",st)
    return st
