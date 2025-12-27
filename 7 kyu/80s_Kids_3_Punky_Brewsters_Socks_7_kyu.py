# 80's Kids #3: Punky Brewster's Socks
# Punky loves wearing different colored socks, but Henry can't stand it.

# Given an array of different colored socks, return a pair depending on who was picking them out.

# Example:

# get_socks('Punky', ['red','blue','blue','green']) -> ['red', 'blue']
# Note that Punky can have any two colored socks, in any order, as long as they are different and both exist. Henry always picks a matching pair.

# If there is no possible combination of socks, return an empty array.

from collections import Counter
def get_socks(name, socks):
    sox =[]
    count = 0
    if len(socks)==0:return []
    print(name,socks)
    if name == "Punky":
        set_one = list(set(socks))
        if len(socks)>=2 and len(set_one)>1:
            return [set_one[0],set_one[1]]
        else:
            return []
        
    else:
        arr = Counter(socks)
        c,n = sorted(arr.items(),key=lambda x:-x[1])[0]
        return [c]*2 if n>=2 else []
        
# def get_socks(name, socks):
#     if name == 'Punky':
#         for s in socks:
#             for y in socks:
#                 if s != y:
#                     return [s, y]
#         return []
#     else:
#         for s in socks:
#             if socks.count(s) > 1:
#                 return [s, s]
#         return []
