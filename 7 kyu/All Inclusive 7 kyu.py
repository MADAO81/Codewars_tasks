# https://www.codewars.com/kata/5700c9acc1555755be00027e/train/python

# def contain_all_rots(strng, arr):
#     rotate = strng
#     if not len(arr) or not strng:
#         return True
#     for i in range(len(strng)):
#         if rotate not in arr:
#             return False
        
#         first_letter = rotate[0]
#         rotate = rotate[1:]
#         rotate += first_letter
        
#     return True

def contain_all_rots(s, l):
    return all(s[i:]+s[:i] in l for i in range(len(s)))
