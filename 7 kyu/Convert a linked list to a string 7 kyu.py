# https://www.codewars.com/kata/582c297e56373f0426000098/train/python


# class Node:
#     def __init__(self, data, next = None):
#         self.data = data
#         self.next = next

# def stringify(node):
#     data = []
#     while node:
#         data.append(str(node.data))
#         node = node.next
#     data.append('None')
#     return ' -> '.join(data)


# def stringify(head):
#     if head is None:
#         return "None"
#     return "{} -> {}".format(head.data, stringify(head.next))



def stringify(list):
    return 'None' if list == None else str(list.data) + ' -> ' + stringify(list.next)
