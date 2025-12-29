# https://www.codewars.com/kata/56e3cd1d93c3d940e50006a4/train/python

# def make_valley(arr):
#     arr = sorted(arr)[::-1]
#     return arr[0::2]+arr[1::2][::-1]

def make_valley(arr):
    arr = sorted(arr, reverse=True) 
    return arr[::2]+arr[1::2][::-1]

