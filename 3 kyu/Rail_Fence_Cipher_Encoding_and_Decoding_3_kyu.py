# https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python

# from itertools import chain

# def fencer(what, n):
#     lst = [[] for _ in range(n)]
#     x,dx = 0,1
#     for c in what:
#         lst[x].append(c)
#         if x==n-1 and dx>0 or x==0 and dx<0: dx *= -1
#         x += dx
#     return chain.from_iterable(lst)
    

# def encode_rail_fence_cipher(s, n): return ''.join(fencer(s,n))
    
# def decode_rail_fence_cipher(s, n):
#     lst = ['']*len(s)
#     for c,i in zip(s, fencer(range(len(s)), n)):
#         lst[i] = c
#     return ''.join(lst)


from itertools import cycle


def rail_pattern(n):
    r = list(range(n))
    return cycle(r + r[-2:0:-1])


def encode_rail_fence_cipher(string, n):
    p = rail_pattern(n)
    
    return ''.join(sorted(string, key=lambda i: next(p)))


def decode_rail_fence_cipher(string, n):
    p = rail_pattern(n)
    indexes = sorted(range(len(string)), key=lambda i: next(p))
    result = [''] * len(string)
    for i, c in zip(indexes, string):
        result[i] = c

    return ''.join(result)
