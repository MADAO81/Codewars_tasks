# Small enough? - Beginner
# You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. If they are, return true. Else, return false.

# You can assume all values in the array are numbers.

def small_enough(array, limit):
    array = sorted(array)
    number = array[-1]
    return number <= limit

# def small_enough(array, limit):
#     return max(array)<=limit
