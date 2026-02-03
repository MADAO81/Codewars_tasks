# https://www.codewars.com/kata/57fe50d000d05166720000b1/train/python

# import re
# def sabb(s, val, happiness):
#     letters = re.findall('[sabbatical]',s)
#     return "Sabbatical! Boom!" if len(letters) + val + happiness > 22 else "Back to your desk, boy."


def sabb(stg, value, happiness):
    sabbatical = (value + happiness + sum(1 for c in stg if c in "sabbatical")) > 22
    return "Sabbatical! Boom!" if sabbatical else "Back to your desk, boy."
