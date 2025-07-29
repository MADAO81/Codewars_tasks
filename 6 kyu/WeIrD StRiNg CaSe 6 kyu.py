# Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, 
# and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, 
# therefore that character should be upper cased and you need to start over for each word.

# The passed in string will only consist of alphabetical characters and spaces(' '). 
# Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

# Examples:
# "String" => "StRiNg"
# "Weird string case" => "WeIrD StRiNg CaSe"

def to_weird_case(words):
    i = 0
    result = ""
    for letter in words:
        if i%2==0:
            result += letter.upper()
        else:
            result += letter.lower()
        if letter == " ":
            i = 0
        else:
            i +=1
    return result


# def to_weird_case_word(string):
#     return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
# def to_weird_case(string):
#     return " ".join(to_weird_case_word(str) for str in string.split())
