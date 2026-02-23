# https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/python

# def smaller(arr):
#     result = []
#     for i in range(len(arr)):
#         count = 0
#         for j in range(i+1,len(arr)):
#             if arr[j]<arr[i]:
#                 count +=1
#         result.append(count)
#     return result


def smaller(arr):
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]
