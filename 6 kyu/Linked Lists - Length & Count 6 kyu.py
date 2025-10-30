# https://www.codewars.com/kata/55beec7dd347078289000021/train/python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def length(x):
    if x is None:
        return 0
    return length(x.next) + 1

  
def count(x,y):
    if x is None:
        return 0
    return count(x.next, y) + (1 if x.data == y else 0)
