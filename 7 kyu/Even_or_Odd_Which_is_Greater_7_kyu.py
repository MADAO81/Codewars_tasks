# https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python


# def even_or_odd(s):
#     even = 0
#     odd = 0
#     for number in s:
#         if int(number) % 2 == 0:
#             even += int(number)
#         else:
#             odd += int(number)
#     if even > odd:
#         return 'Even is greater than Odd'
#     elif even < odd:
#         return 'Odd is greater than Even'
#     else:
#         return 'Even and Odd are the same'



def even_or_odd(s):    
    even_minus_odd = sum([-x if x % 2 else x for x in map(int, s)])
    if even_minus_odd > 0:
        return "Even is greater than Odd"
    elif even_minus_odd < 0:
        return "Odd is greater than Even"
    else:
        return "Even and Odd are the same"
