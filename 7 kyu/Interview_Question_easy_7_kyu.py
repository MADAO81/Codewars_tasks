# https://www.codewars.com/kata/5b358a1e228d316283001892/train/python

# def get_strings(city):
#     result = {}
#     for letter in city.lower():
#         if letter not in result:
#             result[letter] = 1
#         else:
#             result[letter] += 1
#     return ",".join(key + ":" + "*"*value for key, value in result.items() if key != " ")


from collections import Counter

def get_strings(city):
    return ",".join(f"{char}:{'*'*count}" for char, count in Counter(city.replace(" ", "").lower()).items())
