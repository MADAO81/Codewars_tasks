# Simple Fun #132: Number Of Carries
# Task
# Two integer numbers are added using the column addition method. When using this method, some additions of digits produce non-zero carries to the next positions. 
# Your task is to calculate the number of non-zero carries that will occur while adding the given numbers.

# The numbers are added in base 10.

# Example
# For a = 543 and b = 3456, the output should be 0

# For a = 1927 and b = 6426, the output should be 2

# For a = 9999 and b = 1, the output should be 4

# Input/Output
# [input] integer a
# A positive integer.

# Constraints: 1 ≤ a ≤ 10^7

# [input] integer b
# A positive integer.

# Constraints: 1 ≤ b ≤ 10^7

# [output] an integer

def number_of_carries(a, b):
    carry = 0
    count = 0
    digit_a = 0
    digit_b = 0
    sum_digits = 0
    while a >0 or b> 0:
        digit_a = a%10
        digit_b = b%10
        sum_digits = digit_a + digit_b + carry
        carry = sum_digits // 10
        if carry > 0:
            count += 1
        a //= 10
        b //= 10
    return count


# def sum_digits(n: int) -> int:
#     return sum(map(int, str(n)))

# def number_of_carries(a: int, b: int) -> int:
#     return (sum_digits(a) + sum_digits(b) - sum_digits(a + b)) // 9
