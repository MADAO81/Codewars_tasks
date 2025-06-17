# Highest and Lowest
#
# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
#
# Examples
# high_and_low("1 2 3 4 5") # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split()]

    return " ".join([str(max(numbers)), str(min(numbers))])


# def high_and_low(numbers):
#     result_line = []
#     result = ""
#     for i in numbers.split(" "):
#         result_line.append(int(i))
#     result_line = sorted(result_line)
#     result = str(result_line[-1]) + " " + str(result_line[0]) 
#     return result
