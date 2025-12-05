# https://www.codewars.com/kata/568dc69683322417eb00002c/train/python

# def triple_x(s):
#     x = s.find("x")
#     return x != -1 and s.find('xxx') == x

def triple_x(s: str) -> bool:
    return 0 <= s.find("x") == s.find("xxx") 
