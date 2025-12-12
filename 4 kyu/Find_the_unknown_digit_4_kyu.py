# https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python

# def solve_runes(runes):
#     for c in sorted(set('0123456789') - set(runes)):        
#         s = runes.replace('?', c).replace('-', ' - ').replace('+', ' + ').replace('*', ' * ').replace('=', ' == ')
#         if not any(e[0] == '0' and e != '0' for e in s.split()) and eval(s): return int(c)
#     return -1


import re
def solve_runes(runes):
    for symbol in sorted(set('0123456789')-set(runes)):
        to_test = runes.replace('?',symbol)
        if re.search(r'([^\d]|\b)0\d+',to_test):
            continue
        left,right = to_test.split('=')
        if eval(left) == eval(right):
            return int(symbol)
    return -1
