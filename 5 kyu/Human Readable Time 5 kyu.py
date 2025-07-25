# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

import math

def make_readable(seconds):
    h = math.floor(seconds/3600) # hours
    m = math.floor(seconds%3600/60) # minutes
    s = seconds % 3600 % 60 # seconds
    return f"{h:02}:{m:02}:{s:02}"


# def make_readable(seconds):
#     hours, seconds = divmod(seconds, 60 ** 2)
#     minutes, seconds = divmod(seconds, 60)
#     return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)
