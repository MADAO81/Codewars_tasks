# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"



# def get_prime_factors(n):
#     if not isinstance(n,int) or n<=1:
#         if n == 1:
#             return[1]
#         else:
#             return[]
#     else:
#         factors=[]
#         prime=2
#         while prime*prime<=n:
#             while n%prime == 0:
#                 factors.append(prime)
#                 n//=prime
#             prime +=1
#         if n>1:
#             factors.append(n)
#         return factors

# def prime_factors(n):
#     result = ""
#     factors = get_prime_factors(n)
#     for i in sorted(set(factors)):
#         count = factors.count(i)
#         if count == 1:
#             result +="({})".format(i)
#         else:
#             result +="({}**{})".format(i,count)
#     return result

def primeFactors(n):
    i = 2
    r = ''
    while n != 1:
        k = 0
        while n%i == 0:
            n = n / i
            k += 1
        if k == 1:
            r = r + '(' + str(i) + ')'
        elif k == 0: pass
        else:
            r = r + '(' + str(i) + '**' + str(k) + ')'
        i += 1
        
    return r
