# https://www.codewars.com/kata/592fd8f752ee71ac7e00008a/train/python

# import re
# def covfefe(s):
#     result = re.sub(r'\bcoverage\b', 'covfefe', s)
#     if 'coverage' not in s:
#         return s + ' covfefe'    
#     return result

def covfefe(s):
    return s.replace("coverage","covfefe") if "coverage" in s else s+" covfefe"
