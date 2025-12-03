# Implement the function which should return true if given object is a vowel (meaning a, e, i, o, u, uppercase or lowercase), and false otherwise.

# def is_vowel(s): 
#     vowels = 'aeiou'
#     return len(s)==1 and s.lower() in vowels


# def is_vowel(s):
#     return s.lower() in set("aeiou")


# import re

# def is_vowel(s):
#     return True if re.match(r"^[AaEeIiOoUu](?!\n)$", s) else False

import re

def is_vowel(s): 
    pattern = r'^[aeiou]{1}$'
    return bool(re.match(pattern, re.escape(s), re.IGNORECASE))
