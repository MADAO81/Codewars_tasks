# Coding Meetup #2 - Higher-Order Functions Series - Greet developers
# You will be given an array of objects (associative arrays in PHP, tables in COBOL) representing data about developers who have signed up to attend the next coding meetup that you are organising.

# Your task is to return an array where each object will have a new property 'greeting' with the following string value:

# Hi < firstName here >, what do you like the most about < language here >?

# For example, given the following input array:

# list1 = [
#   { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
#   { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
#   { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' } 
# ]
# your function should return the following array:

# [
#   { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java',
#     'greeting': 'Hi Sofia, what do you like the most about Java?'
#   },
#   { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python',
#     'greeting': 'Hi Lukas, what do you like the most about Python?'
#   },
#   { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby',
#     'greeting': 'Hi Madison, what do you like the most about Ruby?'
#   } 
# ]
# Notes:

# The order of the properties in the objects does not matter (except in COBOL).
# The input array will always be valid and formatted as in the example above.


def greet_developers(lst): 
    new_lst = []
    for developer in lst:
        developer.update({"greeting":("Hi " + developer['firstName'] + 
                                      ", what do you like the most about "+ 
                                      developer["language"] + "?")})
        new_lst.append(developer)
    return new_lst
    

# def greet_developers(lst): 
#     for x in lst:
#         x["greeting"] = f"Hi {x['firstName']}, what do you like the most about {x['language']}?"
#     return lst
