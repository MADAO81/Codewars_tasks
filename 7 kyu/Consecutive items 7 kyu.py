# https://www.codewars.com/kata/5f6d533e1475f30001e47514/train/python

# def consecutive(arr, a, b):
#     for i in range(len(arr)-1):
#         if arr[i] == a and arr[i+1] == b:
#             return True
#         elif arr[i+1] == a and arr[i] == b:
#             return True
#     return False


# def consecutive(arr, a, b):
#     x = arr.index(a)
#     y = arr.index(b)
#     return abs(x-y)==1


# def consecutive(arr, a, b):
#     for pair in zip(arr, arr[1:]):
#         if pair == (a, b) or pair == (b, a):
#             return True
#     return False


def consecutive(A, a, b):
    return abs(A.index(a)-A.index(b))==1
