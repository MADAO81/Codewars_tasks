# Colorful Number
# Problem
# Determine whether a non-negative integer number is colorful or not.

# 263 is a colorful number because [2, 6, 3, 2*6, 6*3, 2*6*3] are all different; whereas
# 236 is not colorful, because [2, 3, 6, 2*3, 3*6, 2*3*6] has 6 twice.

# So take all consecutive subsets of digits, take their products, and ensure all the products are different.

# Examples
# 263  -->  true
# 236  -->  false


def colorful(number):
    number = str(number)
    result = set()
    for i in range(len(number)):
        x = 1
        for j in range(i, len(number)):
            x *= int(number[j])
            if x in result: return False
            result.add(x)
    return True
    
    
# from functools import reduce
# from collections import Counter

# def colorful(n):
#     s = list(map(int,str(n)))
#     cnt = Counter( reduce(int.__mul__, s[i:i+x]) for x in range(1,len(s)+1) for i in range(len(s)-x+1))
#     return cnt.most_common(1)[0][1] == 1
