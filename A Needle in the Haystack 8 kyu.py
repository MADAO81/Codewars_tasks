# A Needle in the Haystack
# Can you find the needle in the haystack?
#
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
#
# After your function finds the needle it should return a message (as a string) that says:
#
# "found the needle at position " plus the index it found the needle, so:
#
# Example(Input --> Output)
#
# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

def find_needle(haystack):
    return "found the needle at position " + str(haystack.index("needle"))

# def find_needle(haystack):
#    result = str(haystack.index("needle"))
#    return f"found the needle at position {result}"
