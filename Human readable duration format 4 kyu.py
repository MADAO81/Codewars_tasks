# Human readable duration format
# Your task in order to complete this Kata is to write a function which formats a duration, 
# given as a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero,
# it just returns "now". Otherwise, the duration is expressed as a combination of years, 
# days, hours, minutes and seconds.

# It is much easier to understand with an example:
# * For seconds = 62, your function should return 
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.
# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. 
# In general, a positive integer and one of the valid units of time, separated by a space. 
# The unit of time is used in plural if the integer is greater than 1.
# The components are separated by a comma and a space (", "). Except the last component, 
# which is separated by " and ", just like it would be written in English.
# A more significant units of time will occur before than a least significant one. 
# Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 
# 1 minute and 0 seconds is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function 
# should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component 
# must not be greater than any valid more significant unit of time.

def format_duration(seconds):
    words = ["year", "day", "hour", "minute", "second"]

    if not seconds:
        return "now"
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)

        time = [y, d, h, m, s]

        duration = []

        for x, i in enumerate(time):
            if i == 1:
                duration.append(f"{i} {words[x]}")
            elif i > 1:
                duration.append(f"{i} {words[x]}s")

        if len(duration) == 1:
            return duration[0]
        elif len(duration) == 2:
            return f"{duration[0]} and {duration[1]}"
        else:
            return ", ".join(duration[:-1]) + " and " + duration[-1]
            
            
            
# times = [("year", 365 * 24 * 60 * 60), 
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]

# def format_duration(seconds):

#     if not seconds:
#         return "now"

#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)

#         seconds = seconds % secs

#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]
