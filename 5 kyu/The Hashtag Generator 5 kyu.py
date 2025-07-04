# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

# def generate_hashtag(s):
#     s = "#"+ s.title().replace(" ","") 
#     if  len(s) > 140:
#         return False
#     elif s == "#":
#         return False
#     else:
#         return s


def generate_hashtag(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False
