# Given a string of space separated words, return the longest word.
# If there are multiple longest words, return the rightmost longest word.

# Examples
# "red white blue"  =>  "white"
# "red blue gold"   =>  "gold"


# def longest_word(string_of_words):
#     result = ''
#     for word in string_of_words.split():
#         if len(word)>= len(result):
#             result = word
#     return result



# def longest_word(s):
#     return sorted(s.split(), key = len)[-1]



def longest_word(string_of_words):
    return max(reversed(string_of_words.split()), key=len)
