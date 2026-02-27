# Keypad horror
# Having two standards for a keypad layout is inconvenient!
# Computer keypad's layout:
# "789456123"
# Cell phone keypad's layout:
#  "123456789"
# Solve the horror of unstandardized keypads by providing a function 
# that converts computer input to a number as if it was typed on a phone.

# Example:
# "789" -> "123"

# Notes:
# You get a string with numbers only


# import string
# def computer_to_phone(numbers):
#     keyb_numpad = "789456123"
#     cell_numpad =  "123456789"
#     conv = numbers.translate(str.maketrans(keyb_numpad,cell_numpad))
#     return conv


def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123789', '789123'))
