# https://www.codewars.com/kata/5a8d2bf60025e9163c0000bc/train/python



# def solve(arr):
    
#     from collections import Counter

#     res = []
#     c=Counter(arr)

#     while len(res) != len(arr):
#         for i,v in c.items():
#             if v is max([v for v in c.values()]):
#                 for num in range(v):
#                     res.append(i)
#                 c[i] = 0

#     for i in range(len(res)):
#         for t in range(i,len(res)):
#             if res.count(res[i]) == res.count(res[t]):
#                 if res[t] < res[i]:
#                     res[t],res[i] =  res[i],res[t]

#      return res




# from collections import Counter

# def solve(a):
#     c = Counter(a)
#     return sorted(a, key=lambda k: (-c[k], k))





def solve(arr):
    return sorted(arr, key = lambda x:(-arr.count(x),x))
