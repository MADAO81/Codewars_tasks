# Exclamation marks series #5: Remove all exclamation marks from the end of words
# Task
# Remove all exclamation marks from the end of words. Words are separated by a single space. There are no exclamation marks within a word.

# Examples
# "Hi!" --> "Hi"
# "Hi!!!" --> "Hi"
# "!Hi" --> "!Hi"
# "!Hi!" --> "!Hi"
# "Hi! Hi!" --> "Hi Hi"
# "!!!Hi !!hi!!! !hi" --> "!!!Hi !!hi !hi"

def remove(st):
#     new_st = []
#     for ch in st.split(" "):
#         new_st.append(ch.rstrip("!"))
#     return " ".join(new_st)

    return " ".join([ch.rstrip("!") for ch in st.split(" ")])
