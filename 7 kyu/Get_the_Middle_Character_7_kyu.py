# Get the Middle Character
# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

# If the string's length is odd, return the middle character.
# If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"


# def get_middle(s):
#     half_s = len(s) // 2
#     if len(s)%2 == 0:
#         return s[(half_s - 1):(half_s + 1)]
#     else:
#         return s[half_s:(half_s+1)]


# def get_middle(s):
#     index, odd = divmod(len(s), 2)
#     return s[index] if odd else s[index - 1:index + 1]


def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
