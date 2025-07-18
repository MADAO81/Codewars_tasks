# Which are in?
# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

# Example 1:
# a1 = ["arp", "live", "strong"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns ["arp", "live", "strong"]

# Example 2:
# a1 = ["tarp", "mice", "bull"]

# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

# returns []

# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
# Beware: In some languages r must be without duplicates.

def in_array(array1, array2):
    array3 = []
    for ch2 in array2:
        for ch1 in array1:
            if ch1 in ch2 and ch1 not in array3:
                array3.append(ch1)
    return sorted(array3)

# def in_array(a1, a2):
#     return sorted({sub for sub in a1 if any(sub in s for s in a2)})
