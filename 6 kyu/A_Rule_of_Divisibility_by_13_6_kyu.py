# https://www.codewars.com/kata/564057bc348c7200bd0000ff/train/python

# def thirt(n):
#     multipliers = [1, 10, 9, 12, 3, 4]
#     old_num = 0 
#     new_num = -1000
#     while old_num != new_num:
#         old_num = new_num
#         new_num = 0
#         for i, num in enumerate(list(str(n))[::-1]):
#             new_num += (int(num) * (multipliers[i%6]))
#             n = new_num
#     return new_num


# import itertools as it

# def thirt(n):
#     if n < 100: return n
    
#     pattern = it.cycle([1, 10, 9, 12, 3, 4])
    
#     return thirt(sum(d*n for d,n in zip(map(int, str(n)[::-1]), pattern)))

multipliers = [1, 10, 9, 12, 3, 4]

def thirt(n):
    total = sum([int(c) * multipliers[i % 6] for i, c in enumerate(reversed(str(n)))])
    if n == total:
        return total
    return thirt(total)
