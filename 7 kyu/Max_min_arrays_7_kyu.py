# https://www.codewars.com/kata/5a090c4e697598d0b9000004/train/python

# def solve(arr):
#     arr = sorted(arr)
#     result = []
#     while len(arr)>1:
#         result.append(arr[-1])
#         arr.pop()
#         result.append(arr[0])
#         arr.pop(0)
#     if len(arr) > 0:
#         result.append(arr[0])
#     return result


def solve(arr):
    arr = sorted(arr, reverse=True)
    res = []
    while len(arr):
        res.append(arr.pop(0))
        if len(arr):
            res.append(arr.pop())
    return res
