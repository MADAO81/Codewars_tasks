# https://www.codewars.com/kata/57cc79ec484cf991c900018d/train/python

# def db_sort(arr):
#     return sorted([el for el in arr if isinstance(el, int)]) + sorted([el for el in arr if isinstance(el,str)])

def db_sort(arr): 
    return sorted(arr, key=lambda x: (isinstance(x,str),x))
