# https://www.codewars.com/kata/61123a6f2446320021db987d/train/python

# def prev_mult_of_three(n):
#     return prev_mult_of_three(n//10) if n%3 else n or None


# def prev_mult_of_three(n):
#     if n == 0:
#         return None
#     elif n % 3 == 0:
#         return n
#     else:
#         return prev_mult_of_three(n // 10)




def prev_mult_of_three(n):
    while n % 3 :
        n //= 10
    return n or None
