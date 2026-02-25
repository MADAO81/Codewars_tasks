# Is it a vowel on this position?
# Check if it is a vowel(a, e, i, o, u,) on the n position in a string (the first argument). Don't forget about uppercase.

# A few cases:

# {
# checkVowel('cat', 1)  ->   true // 'a' is a vowel
# checkVowel('cat', 0)  ->   false // 'c' is not a vowel
# checkVowel('cat', 4)  ->   false // this position doesn't exist
# }
# P.S. If n < 0, return false


# def check_vowel(strng, position):
#     strng = strng.lower()
#     vowel_list = ["a","e","i","o","u"]
#     if position < 0 or position > len(strng):
#         return False
#     if strng[position] in vowel_list:
#         return True
#     return False


def check_vowel(s,i):
    return 0 <= i < len(s) and s[i] in "aieouAEIOU"
