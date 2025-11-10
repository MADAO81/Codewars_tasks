# https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python

# def path_finder(maze):
#     maze = maze.split('\n')
#     n = len(maze)
#     queue = dict()
#     queue[(n - 1, n - 1)] = 0
#     cache = set()
#     moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     while queue:
#         k, v = queue.popitem()
#         current_row, current_col = k
#         if current_row == current_col ==  0:
#             return True
#         cache.add((current_row, current_col))
#         for move in moves:
#             nxt_row, nxt_col = current_row + move[0], current_col + move[1]
#             if (nxt_row, nxt_col) in cache:
#                 continue
#             elif not (0 <= nxt_row < n) or not (0 <= nxt_col < n):
#                 continue
#             elif maze[nxt_row][nxt_col] == 'W':
#                 continue
#             queue[(nxt_row, nxt_col)] = 0
#     return False


def path_finder(maze):
    matrix = list(map(list, maze.splitlines()))
    stack, length = [[0, 0]], len(matrix)
    while len(stack):
      x, y = stack.pop()
      if matrix[x][y] == '.':
        matrix[x][y] = 'x'
        for x, y in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
          if 0 <= x < length and 0 <= y < length:
            stack.append((x, y))
    return matrix[length-1][length-1] == 'x'
