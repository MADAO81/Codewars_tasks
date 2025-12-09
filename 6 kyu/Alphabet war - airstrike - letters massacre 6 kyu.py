# https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/python



# def alphabet_war(fight):
#     force = { 'w': 4, 'p': 3, 'b': 2, 's': 1, 'm': -4, 'q': -3, 'd': -2, 'z': -1} 
#     l = list(' ' + fight + ' ')
#     for i,ch in enumerate(l):
#         if ch == '*':
#             l[i-1] = '_'
#             l[i] = '_'
#             l[i+1] = '_' if l[i+1] != '*' else '*'
#     result = sum(force.get(ch,0) for ch in l)
#     if result > 0:
#         return "Left side wins!"
#     elif result < 0:
#         return "Right side wins!"
#     elif result == 0:
#         return "Let's fight again!"

import re

powers = {
    'w': -4, 'p': -3, 'b': -2, 's': -1,
    'm': +4, 'q': +3, 'd': +2, 'z': +1,
}

def alphabet_war(fight):
    fight = re.sub('.(?=\*)|(?<=\*).', '', fight)
    result = sum(powers.get(c, 0) for c in fight)
    if result < 0:
        return 'Left side wins!'
    elif result > 0:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
