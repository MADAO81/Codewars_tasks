# https://www.codewars.com/kata/55b4d87a3766d9873a0000d4/train/python

# def howmuch(m, n):
#     result = []
#     for x in range(min(m,n), max(m,n)+1):
#         a,b = x - 2, x-1
#         if a % 7 == 0 and b % 9 == 0:
#             result.append([f'M: {x}', f'B: {a//7}', f'C: {b//9}'])
#     return result


# def howmuch(m, n):
#     i = min(m, n)
#     j = max(m, n)
#     res = []
#     while (i <= j):
#         if ((i % 9 == 1) and (i %7 == 2)):
#             res.append(["M: " + str(i), "B: " + str(i // 7), "C: " + str(i // 9)])
#         i += 1
#     return res




def howmuch(m, n):    
    return [['M: %d'%i, 'B: %d'%(i/7), 'C: %d'%(i/9)] for i in range(min(m,n), max(m,n)+1) if i%7 == 2 and i%9 == 1]
