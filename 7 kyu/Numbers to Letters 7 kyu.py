# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c/train/python

# from string import ascii_lowercase

# def switcher(arr):
#     char_pool = [*reversed([*ascii_lowercase]), "!", "?", " "]
#     return "".join([char_pool[int(num) - 1] for num in arr])


chars = "_zyxwvutsrqponmlkjihgfedcba!? "

def switcher(arr):
    return "".join(chars[int(i)] for i in arr if i != "0")
