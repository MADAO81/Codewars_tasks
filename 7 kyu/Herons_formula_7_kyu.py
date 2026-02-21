# Heron's formula
# Write function heron which calculates the area of a triangle with sides a, b, and c 

# import math
# def heron(a, b, c):
#     s = (a + b + c) / 2
#     return math.sqrt(s *(s-a)*(s-b)*(s-c))
    
def heron(a, b, c):
    s = (a + b + c) / 2
    return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)
