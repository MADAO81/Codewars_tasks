# What is between?
# Complete the function that takes two integers (a, b, where a < b) and return 
# an array of all integers between the input parameters, including them.

# For example:

# a = 1
# b = 4
# --> [1, 2, 3, 4]

def between(a,b):
    result = []
    for i in range(a,b+1):
        result.append(i)
    return result
    
    
# def between(a,b):
#     return list(range(a,b+1))