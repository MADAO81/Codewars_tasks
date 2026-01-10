# Balanced Number (Special Numbers Series #1 )
# https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python

def balanced_num(number):
    s = str(number)
    l = (len(s)-1)//2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"
