# Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages
# You will be given an array of objects (associative arrays in PHP, table in COBOL, dictionaries in Python)
# representing data about developers who have signed up to attend the next coding meetup that you are organising.

# Your task is to return an object (associative array in PHP, table in COBOL, dictionary in Python) 
# which includes the count of each coding language represented at the meetup.

# For example, given the following input array:

# list1 = [
#     { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
#     { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
#     { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
#     { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
#     ]

def count_languages(lst): 
    lang = {}
    for dev in lst:
        if dev["language"] in lang:
            lang[dev["language"]] += 1
        else:
            lang[dev["language"]] = 1
    return lang
    

# from collections import Counter
# def count_languages(lst): 
#     return Counter([d['language'] for d in lst])
