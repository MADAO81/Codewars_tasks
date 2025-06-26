# Coding 3min : A*B=C
# This is the simple version of Fastest Code series. If you need some challenges, please try the Performance version

# Task:
# Give you a number array numbers and a number c.

# Find out a pair of numbers(we called them number a and number b) from the array numbers, let a*b=c, result format is an array [a,b]

# The array numbers is a sorted array, value range: -100...100

# The result will be the first pair of numbers, for example,findAB([1,2,3,4,5,6],6) should return [1,6], instead of [2,3]

# Please see more example in testcases.

def find_a_b(numbers, c):
    for i, m in enumerate(numbers,1):
        for n in numbers[i:]:
            if m * n == c:
                return [m, n]
    return None


# from itertools import combinations

# def find_a_b(numbers,c):
#     return next(([a,b] for a,b in combinations(numbers,2) if a*b==c),None)
