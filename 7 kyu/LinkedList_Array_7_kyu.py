# https://www.codewars.com/kata/557dd2a061f099504a000088/train/python

# def list_to_array(node):
#     return ([node.value] + list_to_array(node.next)) if node else []


def list_to_array(lst):
    arr = []
    while lst != None:
        arr.append(lst.value)
        lst = lst.next
    return arr
