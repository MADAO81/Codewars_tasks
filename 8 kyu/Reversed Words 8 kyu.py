# Complete the solution so that it reverses all of the words within the string passed in.

# Words are separated by exactly one space and there are no leading or trailing spaces.

# Example(Input --> Output):

# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

# def reverse_words(s):
#     first_step = s.split(" ")
#     first_step.reverse()
#     return " ".join(first_step)


def reverseWords(str):
    return " ".join(str.split(" ")[::-1])
