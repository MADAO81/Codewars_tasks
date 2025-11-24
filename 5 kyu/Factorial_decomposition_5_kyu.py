# https://www.codewars.com/kata/5a045fee46d843effa000070/train/python

# def primes(n):
# #         return all primes number of n
#     p = 2
#     res = []
#     while p * p <= n:
#         while n%p == 0:
#             res.append(p)
#             n //= p
#         p +=1
#     if n>1:
#         res.append(n)
#     return res

# def decomp(n):
#     fctrs = {}
#     result = ''
    
#     while n > 1:
#         tp = primes(n)
#         n -=1
#         for i in set(tp):
#             if i in fctrs:
#                 fctrs[i] += tp.count(i)
#             else:
#                 fctrs[i] = tp.count(i)
#     fctrs = sorted(fctrs.items(), key=lambda x: x[1])
#     fctrs.reverse()
    
#     for i in fctrs:
#         if i[1] == 1:
#             result += f"{i[0]}"
#         else:
#             result += f"{i[0]}^{i[1]}"
#         if i != fctrs[-1]:
#             result += " * "
            
#     return result



from collections import defaultdict

def dec(n):
    decomp = defaultdict(lambda:0)
    i = 2
    while n > 1:
        while n % i == 0:
            n /= i
            decomp[i] += 1
        i += 1
    return decomp
            

def decomp(n):
    ans = defaultdict(lambda:0)
    for i in range(2, n + 1):
        for key, value in dec(i).items():
            ans[key] += value
    return ' * '.join('{}^{}'.format(x, y) if y > 1 else str(x) for x, y in sorted(ans.items()))
