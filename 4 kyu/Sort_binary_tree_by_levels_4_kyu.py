# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python

# def tree_by_levels(node):
#     if node is None:
#         return []
    
#     level = [node]
#     levels = [[node.value]]
    
#     while len(level) != 0:
#         level = [y for x in level for y in (x.left, x.right) if y is not None]
#         levels.append([x.value for x in level])
        
#     return [x for xs in levels for x in xs]


from collections import deque


def tree_by_levels(node):
    if not node:
        return []
    res, queue = [], deque([node,])
    while queue:
        n = queue.popleft()
        res.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)
    return res
