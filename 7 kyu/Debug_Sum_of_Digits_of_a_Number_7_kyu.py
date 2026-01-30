# Debug   function getSumOfDigits that takes positive integer to calculate sum of its digits. Assume that argument is an integer.

# Example
# 123  => 6
# 223  => 7
# 1337 => 14

# def get_sum_of_digits(num):
#     return sum(map(int, str(num)))

def get_sum_of_digits(num):
    sum = 0
    digits = str(num)
    for x in digits:
        sum += int(x)
    return sum
