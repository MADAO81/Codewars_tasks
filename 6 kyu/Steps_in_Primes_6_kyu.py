# https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python



# def step(g, m, n):
#     prime_list = []
#     for num in range(m,n):
#         number_prime = is_prime(num)
#         prime_list.append(number_prime)
#         if number_prime == True:
#             if len(prime_list) > g:
#                 if prime_list[num-g-m] == True:
#                     return [num-g, num]
#             else:
#                 previous_prime = num
    
# def is_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#         elif i*i > num:
#             return True
#     return True




# def is_prime(num):
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#         elif i*i > num:
#             return True
#     return True


# def step(g, m, n):
#     for i in range(m, n-g+1):
#         if is_prime(i) and is_prime(i+g):
#             return [i, i+g]





from gmpy2 import is_prime

def step(g, m, n):
    for i in range(m, n-g+1):
        if is_prime(i) and is_prime(i+g):
            return [i, i+g]
