# https://www.codewars.com/kata/5a946d9fba1bb5135100007c/train/python


# from itertools import count

# def isPrime(n):
#     return n == 2 or n%2 and all(n%x for x in range(3,int(n**.5)+1,2))

# def minimum_number(numbers):
#     s = sum(numbers)
#     return next(x for x in count(0) if isPrime(s+x) )



def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def minimum_number(numbers):
    s = sum(numbers)
    while is_prime(s) != True:
        s += 1
    return s - sum(numbers)
