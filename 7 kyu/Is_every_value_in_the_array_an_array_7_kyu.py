# https://www.codewars.com/kata/582c81d982a0a65424000201/train/python


# def arr_check(arr):
#     flag = True
#     for ch in arr:
#         if type(ch) == list:
#             flag = True
#         else:
#             flag = False
#     return flag


# def arr_check(arr):
#     return all(isinstance(el, list) for el in arr)


def arr_check(arr):
    return all(type(i) == list for i in arr)
