# https://www.codewars.com/kata/569924899aa8541eb200003f/train/python

# from string import ascii_uppercase

# AZ = dict(zip(' ' + ascii_uppercase, range(27)))


# def quicksum(packet):
#     result = 0
#     for i, a in enumerate(packet, 1):
#         try:
#             result += AZ[a] * i
#         except KeyError:
#             return 0
#     return result


def quicksum(packet):
    result = 0
    
    for idx, char in enumerate(packet, 1):
        if char.isupper():
            result += idx * (ord(char) - 64)
        elif char == " ":
            continue
        else:
            return 0
    
    return result
