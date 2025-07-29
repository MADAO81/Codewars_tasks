# In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. 
# For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

# Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) 
# or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

# More details about factorial can be found here.

def factorial(n):
    total = 1;
    if n < 0 or n > 12:
        raise ValueError("Value outside of allowable range.");
    else:
        while n > 0:
            total *= n;
            n -= 1;
    return total

# def factorial(n):
#     if n < 0 or n > 12:
#         raise ValueError
#     return 1 if n <= 1 else n*factorial(n-1)


# from math import factorial as fac

# def factorial(n):
#     if n < 0 or 12 < n:
#         raise ValueError
#     return fac(n)
