# Clean Nesting Tree
# Task:

# You are given a main list that may contain nested lists of arbitrary depth. 
# Imagine this structure as a tree, where each list is a node and its elements are child nodes.
# Your task is to implement a function that checks whether the entire structure follows the nesting rule:
# At each level (depth) of the tree, each node's children must all either be:
# dead ends (empty lists [])
# nested lists
# Examples
# [ [ [[]], [[]], [[]]  ], [[]] , [[]]  ] -> True
# [] -> True
# [ [], [] ] -> True
# [ [ [], [], []  ] , [ [], [[]]  ] ]  -> False

def is_cleanly_nested(arr):
    if not arr:
        return True
    first_empty = not arr[0]
    for element in arr:
        if (not element) != first_empty:
            return False
        if not is_cleanly_nested(element):
            return False
    return True
