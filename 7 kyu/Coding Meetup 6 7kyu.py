# Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?
# You will be given an array of objects (associative arrays in PHP, tables in COBOL) representing data
# about developers who have signed up to attend the next coding meetup that you are organising.

# Your task is to return either:

# true if all developers in the list code in the same language; or
# false otherwise.
# For example, given the following input array:

# list1 = [
#   { 'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42, 'language': 'JavaScript' },
#   { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22, 'language': 'JavaScript' },
#   { 'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65, 'language': 'JavaScript' },
# ]
# your function should return true.

# Notes:

# The strings representing a given language will always be formatted in the same way
# (e.g. 'JavaScript' will always be formatted will upper-case 'J' and 'S'
# The input array will always be valid and formatted as in the example above.

def is_same_language(lst): 
    languages = []
    for dev in lst:
        if len(languages) > 1:
            return False
        if dev["language"] not in languages:
            languages.append(dev["language"])
    if len(languages) > 1:
        return False
    return True
    
#  def is_same_language(lst): 
#    return len(set(i["language"] for i in lst)) == 1
