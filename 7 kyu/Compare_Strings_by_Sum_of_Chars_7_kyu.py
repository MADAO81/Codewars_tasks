# https://www.codewars.com/kata/576bb3c4b1abc497ec000065/train/python

# def compare(s1,s2):
#     c1 = c2 = 0

#     if s1 and s1.isalpha():
#         c1 += sum(ord(i.upper()) for i in s1)
    
#     if s2 and s2.isalpha():
#         c2 += sum(ord(i.upper()) for i in s2)
    
#     return c1 == c2




# def compare(s1,s2):
#     f = lambda x: sum(map(ord,x.upper())) if x and x.isalpha() else ''
#     return f(s1) == f(s2)



def string_cnt(s):
    try:
        if s.isalpha():
            return sum(ord(a) for a in s.upper())
    except AttributeError:
        pass
    return 0


def compare(s1, s2):
    return string_cnt(s1) == string_cnt(s2)
