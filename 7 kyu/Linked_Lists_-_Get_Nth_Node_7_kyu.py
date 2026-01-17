# https://www.codewars.com/kata/55befc42bfe4d13ab1000007/train/python

# class Node(object):
#   def __init__(self, data):
#     self.data = data
#     self.next = None
    
# def get_nth(node, index):
#   if node and index >= 0: return node if index < 1 else get_nth(node.next, index - 1)
#   raise ValueError


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    v = -1
    n = node
    while n:
        v += 1
        if v == index:
        	return n
        n = n.next
    
    raise ValueError
