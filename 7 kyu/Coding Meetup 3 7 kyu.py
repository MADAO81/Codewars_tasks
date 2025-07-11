# Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?
# You will be given an array of objects (associative arrays in PHP) representing data about developers
# who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return:
#
# true if at least one Ruby developer has signed up; or
# false if there will be no Ruby developers.
# For example, given the following input array:
#
# list1 = [
#     { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
#     'language': 'Java' },
#     { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
#     'language': 'Python' },
#     { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas',
#     'age': 32, 'language': 'Ruby' }
#     ]
# your function should return true.
#
# Notes:
#
# The input array will always be valid and formatted as in the example above.

def is_ruby_coming(lst):
    for developer in lst:
        if developer["language"] == "Ruby":
            return True
    return False

# def is_ruby_coming(lst):
#     return any(x["language"] == "Ruby" for x in lst)