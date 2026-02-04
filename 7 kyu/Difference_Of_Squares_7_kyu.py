# https://www.codewars.com/kata/558f9f51e85b46e9fa000025/train/python

# def difference_of_squares(x):
#     r = range(1,x+1,1)
#     return (sum(r) ** 2) - (sum( z**2 for z in r))

def difference_of_squares(n):
    square_of_sum = 0
    sum_of_square = 0
    for i in range(n+1):
        square_of_sum += i
        sum_of_square += i**2
    return square_of_sum**2 - sum_of_square
