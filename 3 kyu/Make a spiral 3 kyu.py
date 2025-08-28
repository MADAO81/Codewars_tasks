# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/solutions/python

# def spiralize(size):
    
#     def on_board(x, y):
#         return 0 <= x < size and 0 <= y < size
        
#     def is_one(x, y):
#         return on_board(x, y) and spiral[y][x] == 1
        
#     def can_move():
#         return on_board(x+dx, y+dy) and not (is_one(x+2*dx, y+2*dy) or is_one(x+dx-dy, y+dy+dx) or is_one(x+dx+dy, y+dy-dx))
    
    
#     spiral = [[0 for x in range(size)] for y in range(size)]   
#     x, y = -1, 0
#     dx, dy = 1, 0
#     turns = 0
    
#     while (turns < 2):
#         if can_move():
#             x += dx
#             y += dy
#             spiral[y][x] = 1
#             turns = 0
#         else:
#             dx, dy = -dy, dx
#             turns += 1
    
#     return spiral


# def spiralize(size):
#     matrix = list(map(lambda x: list(map(lambda y:1 if (int(size + 1)/2)%2 == 1 else 0, range(0,size))), range(0,size)))
#     spiral = 1
#     for i in range(0, int(size/2)):
#         for u in range(0,size - i*2):
#             matrix[i][u+i] = spiral
#             matrix[u+i][i] = spiral
#             matrix[size-i-1][u+i] = spiral
#             matrix[u+i][size-i-1] = spiral
            
#             if size % 4 == 0:
#                 if i != int(size/2)-1:
#                     matrix[i+1][i]=1 - spiral
#             else:
#                 matrix[i+1][i] = 1 - spiral
#         spiral = 1 - spiral
#     return matrix

import numpy as np

def spiralize(size):
    if size == 0:
        return []
    if size == 1:
        return [[1]]
    if size == 2:
        return [[1,1],[0,1]]
    sp = np.zeros((size, size))
    sp[0, :] = 1
    sp[:, -1] = 1
    sp[-1, :] = 1
    sp[2:, :-2] = np.array(spiralize(size-2))[::-1,::-1]
    return sp.tolist()
