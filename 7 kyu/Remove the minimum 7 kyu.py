# The museum of incredibly dull things
# The museum of incredibly dull things wants to get rid of some exhibits. 
# Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

# However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. 
# If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples
# * Input: [1,2,3,4,5], output = [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]



def remove_smallest(numbers):
    result = numbers.copy()
    if len(numbers)<1:
        return []
    min_value = min(result)
    min_index = result.index(min_value)
    del result[min_index]
    return result

# def remove_smallest(numbers):
#     a = numbers[:]
#     if a:
#         a.remove(min(a))
#     return a
