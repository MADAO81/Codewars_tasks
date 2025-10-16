# When provided with a String, capitalize all vowels
# For example:
# Input : "Hello World!"
# Output : "HEllO WOrld!"
# Note: Y is not a vowel in this kata.



# def swap(st):
#     result = ''
#     vow = 'aeuoi'
#     for letter in st:
#         if letter in vow:
#             result += letter.capitalize()
#         else:
#             result += letter
#     return result


def swap(st):
  tr = str.maketrans('aeiou', 'AEIOU')
  return st.translate(tr);
