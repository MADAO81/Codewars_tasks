# https://www.codewars.com/kata/5966847f4025872c7d00015b/train/python


# from math import floor
# from statistics import mean 

# def average_string(s):
#     s = s.split()
#     numbers_dict = {"zero":0, "one":1, "two":2,
#                    "three":3, "four":4, "five":5,
#                    "six":6, "seven":7, "eight":8,
#                    "nine":9}
#     nums_sum = []
#     if not s:
#         return "n/a"
#     for number in s:
#         if number not in numbers_dict:
#             return "n/a"
#     for idx,number in enumerate(s):
#         if number in numbers_dict:
#             nums_sum.insert(idx,numbers_dict[number])
#     return list(numbers_dict.keys())[list(numbers_dict.values()).index(floor(mean(nums_sum)))]



# def average_string(s):
#     if not s:
#         return 'n/a'

#     numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     total = 0
#     counter = 0
#     for n in s.split():
#         try:
#             value = numbers.index(n)
#             total += value
#             counter += 1
#         except:
#             return 'n/a'
#     return numbers[total // counter]


N = ['zero','one','two','three','four','five','six','seven','eight','nine']

def average_string(s):
    try:
        return N[sum(N.index(w) for w in s.split()) // len(s.split())]
    except (ZeroDivisionError, ValueError):
        return 'n/a'
