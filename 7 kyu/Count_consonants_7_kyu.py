# https://www.codewars.com/kata/564e7fc20f0b53eb02000106/train/python

# def consonant_count(s):
#     vowels ='aeiou'
#     count = 0
#     s = s.replace(" ", "").lower()
#     for letter in s:
#         if letter not in vowels  and not letter.isnumeric() and letter.isalnum():
#             count +=1
#     return count

def consonant_count(str):
    return sum(1 for c in str if c.isalpha() and c.lower() not in "aeiou")
