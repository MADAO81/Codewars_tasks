# https://www.codewars.com/kata/56efab15740d301ab40002ee/train/python


# from math import gcd

# def gcdi(x,y):
#     return gcd(x, y)
 
# def lcmu(a, b):
#     return abs(a*b) // gcd(a, b)

# def som(a, b):
#     return a + b

# def maxi(a, b):
#     return max(a, b)

# def mini(a, b):
#     return min(a, b)

# def oper_array(fct, arr, init): 
#     retArray = []
#     for i, item in enumerate(arr): retArray.append(fct(retArray[-1], item) if i != 0 else fct(init, item))
#     return retArray


def gcdi(a, b):
    from fractions import gcd
    return abs(gcd(a,b))
def lcmu(a, b):
    from fractions import gcd
    return abs(a*b//gcd(a,b))
def som(a, b):
    return a + b
def maxi(a, b):
    return max(a,b)
def mini(a, b):
    return min(a,b)
def oper_array(fct, arr, init): 
    out = [init]
    
    for i in range(len(arr)):
        out.append(fct(out[-1], arr[i]))
    return out[1:]
