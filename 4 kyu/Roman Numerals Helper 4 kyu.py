# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python


class RomanNumerals:

    @staticmethod
    def to_roman(arabic_number):
        """ This function converts an arabic number (int) into a roman number (str) """
        roman_numbers_symbol_value = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("XXX", 30), ("XX", 20),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        roman_num = ""
        for symbol, value in roman_numbers_symbol_value:
            while arabic_number >= value:
                arabic_number -= value
                roman_num += symbol
        return roman_num

    @staticmethod
    def from_roman(roman_num):
        """ This function converts a roman number (str) into an arabic number (int)"""
        roman_numbers_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        # Base case (only the last symbol remains to be evaluated)
        if len(roman_num) == 1:
            return roman_numbers_dict[roman_num]
        # Recursive case (all other symbols of the roman number except the first)
        tail = roman_num[1:len(roman_num)]
        # Decimal value of the first symbol
        current_value = roman_numbers_dict[roman_num[0]]
        # Comparison of present value with previous value
        if current_value >= roman_numbers_dict[roman_num[1]]:
            # present value greater or equal than previous value
            return current_value + RomanNumerals.from_roman(tail)
        else:
            # present value less than previous value
            return -current_value + RomanNumerals.from_roman(tail)


# from collections import OrderedDict
# import re


# ROMAN_NUMERALS = OrderedDict([
#     ('M', 1000),
#     ('CM', 900),
#     ('D', 500),
#     ('CD', 400),
#     ('C', 100),
#     ('XC', 90),
#     ('L', 50),
#     ('XL', 40),
#     ('X', 10),
#     ('IX', 9),
#     ('V', 5),
#     ('IV', 4),
#     ('I', 1),
# ])

# DECIMAL_TO_ROMAN = [(v, k) for k, v in ROMAN_NUMERALS.items()]

# ROMAN_RE = '|'.join(ROMAN_NUMERALS)


# class RomanNumerals(object):
#     @staticmethod
#     def from_roman(roman):
#         return sum(ROMAN_NUMERALS[d] for d in re.findall(ROMAN_RE, roman))

#     @staticmethod
#     def to_roman(decimal):
#         result = []
#         for number, roman in DECIMAL_TO_ROMAN:
#             while decimal >= number:
#                 decimal -= number
#                 result.append(roman)
#         return ''.join(result)
