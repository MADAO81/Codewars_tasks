# https://www.codewars.com/kata/5508249a98b3234f420000fb/train/python

# from string import ascii_letters as al
# from itertools import accumulate

# def caesar(l, k):
#     sh = ord('a' if l.islower() else 'A')
#     return chr((ord(l) - sh + k) % 26 + sh) if l in al else l

# def moving_shift(s, shift):
#     caes = [caesar(l, shift+k) for k,l in enumerate(s)]
#     if len(caes) % 5 == 0:
#         lns = list(accumulate([len(caes) // 5] * 5))
#     else:
#         d,r = divmod(len(caes), len(caes) // 5 + 1)
#         lns = list(accumulate([len(caes) // 5 + 1] * d + [r] + [0] * (5-d-1)))
        
#     return [''.join(caes[x:y]) for x,y in zip([0]+lns, lns)]

# def demoving_shift(s, shift):
#     return ''.join(caesar(l, -shift-k) for k,l in enumerate(''.join(s)))


from string import ascii_lowercase as abc, ascii_uppercase as ABC
from math import ceil

def _code(string, shift, mode):
    return ''.join(
        abc[(abc.index(c) + i*mode + shift) % len(abc)] if c in abc else
        ABC[(ABC.index(c) + i*mode + shift) % len(ABC)] if c in ABC else c
        for i, c in enumerate(string))

def moving_shift(string, shift):
    encoded = _code(string, shift, 1)
    cut = int(ceil(len(encoded) / 5.0))
    return [encoded[i : i+cut] for i in range(0, 5 * cut, cut)]

def demoving_shift(arr, shift):
    return _code(''.join(arr), -shift, -1)
