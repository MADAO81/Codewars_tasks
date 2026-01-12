#  https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python

# def is_interesting(number, awesome_phrases):
#     if number + 1 in awesome_phrases or number + 2 in awesome_phrases:
#         return 1
#     if number in awesome_phrases:
#         return 2
#     if interesting_number(number):
#         return 2
#     if interesting_number(number+1) or interesting_number(number+2):
#         return 1
#     return 0
    

# def interesting_number(number):
#     if number % 100 == number: # Check if number is 3 digit or more
#         return False
#     if number % 100 == 0: # Check for digit followed by all zeroes
#         return True 
#     number = str(number)
#     if len(set(number)) == 1:  # check for number having same digits
#         return True
#     if number[::-1] == number: # check for palindrome
#         return True
#     if number in '1234567890': # sequential increasing
#         return True
#     if number in '9876543210': # sequential decreasing
#         return True


def is_incrementing(number): 
    return str(number) in '1234567890'
def is_decrementing(number): 
    return str(number) in '9876543210'
def is_palindrome(number):   
    return str(number) == str(number)[::-1]
def is_round(number):        
    return set(str(number)[1:]) == set('0')

def is_interesting(number, awesome_phrases):
    tests = (is_round, is_incrementing, is_decrementing,
             is_palindrome, awesome_phrases.__contains__)
       
    for num, color in zip(range(number, number+3), (2, 1, 1)):
        if num >= 100 and any(test(num) for test in tests):
            return color
    return 0
