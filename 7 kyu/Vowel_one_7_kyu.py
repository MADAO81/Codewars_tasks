# https://www.codewars.com/kata/580751a40b5a777a200000a1/train/python

# def vowel_one(s):
#     vowels = 'aeiou'
#     result = ''
#     for symbol in s.lower():
#         if symbol in vowels:
#             result += '1'
#         else:
#             result += '0'
#     return result

def vowel_one(s):
    return ''.join(['1' if symbol in 'aeiou' else '0' for symbol in s.lower()])
    
