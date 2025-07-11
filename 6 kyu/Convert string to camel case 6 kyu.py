# Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
# The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, 
# also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"

# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"



import re
def to_camel_case(text):
    new_text = re.sub("[_-]\w", lambda x: x.group()[-1:].capitalize(), text)
    return new_text

# def to_camel_case(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#     if len(removed) == 0:
#         return ''
#     return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])


# import re

# def to_camel_case(text):
#     words = re.split(r'[-_]', text)
#     words[1:] = list(map(str.capitalize, words[1:]))
#     return "".join(words)
