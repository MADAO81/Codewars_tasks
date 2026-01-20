# https://www.codewars.com/kata/57ee24e17b45eff6d6000164/train/python


# def cat_mouse(x):
#     dots = 0
#     for ch in x:
#         if ch == ".":
#             dots +=1
#     if dots <= 3:
#         return "Caught!"
#     return "Escaped!"

def cat_mouse(x):
    return 'Escaped!' if x.count('.') > 3 else 'Caught!'
