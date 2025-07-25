# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100
# Attention: If the number has leading zeros the amount of digits should be considered.

import re
def increment_string(strng):
    number = re.findall(r"\d+",strng)
    if not strng:
        return "1"
    elif strng[-1] not in "0123456789":
        return strng + "1"
    elif number:
        strng_number = number[-1]
        strng = strng.rsplit(strng_number,1)[0]
        number = str(int(strng_number)+1)
        return strng + "0"*(len(strng_number)-len(number))+number


# def increment_string(strng):
#     head = strng.rstrip('0123456789')
#     tail = strng[len(head):]
#     if tail == "": return strng+"1"
#     return head + str(int(tail) + 1).zfill(len(tail))
