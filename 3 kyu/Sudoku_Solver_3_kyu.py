# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

def sudoku(P):

    for row, col in [(r, c) for r in range(9) for c in range(9) if not P[r][c]]:
            
        rr, cc = (row // 3) * 3, (col // 3) * 3
            
        use = {1,2,3,4,5,6,7,8,9} - ({P[row][c] for c in range(9)} | {P[r][col] for r in range(9)} | {P[rr+r][cc+c] for r in range(3) for c in range(3)})

        if len(use) == 1:
            P[row][col] = use.pop()
            return sudoku(P)
    return P


# assignments = []
# rows = 'ABCDEFGHI'
# cols = '123456789'

# def assign_value(values, box, value):
#     """
#     Please use this function to update your values dictionary!
#     Assigns a value to a given box. If it updates the board record it.
#     """

#     # Don't waste memory appending actions that don't actually change any values
#     if values[box] == value:
#         return values

#     values[box] = value
#     if len(value) == 1:
#         assignments.append(values.copy())
#     return values

# def naked_twins(values):
#     """Eliminate values using the naked twins strategy.
#     Args:
#         values(dict): a dictionary of the form {'box_name': '123456789', ...}

#     Returns:
#         the values dictionary with the naked twins eliminated from peers.
#     """
#     for unit in unitlist:
#         count_map = {} # to store mapping of value => counts
#         value_to_box = {} # to store mapping from value => box
#         for box in unit:
#             value = values[box]
#             if len(value) == 2:
#                 if value in count_map:
#                     count_map[value] += 1
#                 else:
#                     count_map[value] = 1
#                 if value in value_to_box:
#                     value_to_box[value].append(box)
#                 else:
#                     value_to_box[value] = [box]
#         for value, count in count_map.items():
#             if count == 2:
#                 boxes_with_value = value_to_box[value]
#                 common_peers = peers[boxes_with_value[0]].intersection(peers[boxes_with_value[1]]) # Common values to both units should be considered
#                 for peer in common_peers:
#                     for char in value:
#                         values = assign_value(values, peer, values[peer].replace(char, ""))
#     return values

# def cross(A, B):
#     "Cross product of elements in A and elements in B."
#     return [s+t for s in A for t in B]

# boxes = cross(rows, cols)
# row_units = [cross(r, cols) for r in rows]
# column_units = [cross(rows, c) for c in cols]
# square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
# unitlist = row_units + column_units + square_units
# units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
# peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

# def grid_values(grid):
#     """
#     Convert grid into a dict of {square: char} with '123456789' for empties.
#     Args:
#         grid(string) - A grid in string form.
#     Returns:
#         A grid in dictionary form
#             Keys: The boxes, e.g., 'A1'
#             Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
#     """
#     sudoku_values = ['123456789' if elem is "." else elem for elem in list(grid)]
#     return dict(zip(boxes, sudoku_values))

# def display(values):
#     grid = []
#     for i in range(9):
#         grid.append([0]*9)
#     for box in boxes:
#         row_index = rows.find(box[0])
#         col_index = cols.find(box[1])
#         grid[row_index][col_index] = int(values[box])
#     return grid

# def eliminate(values):
#     solved_values = [box for box in values.keys() if len(values[box]) == 1]
#     for box in solved_values:
#         digit = values[box]
#         for peer in peers[box]:
#             assign_value(values, peer, values[peer].replace(digit, ''))
#     return values

# def only_choice(values):
#     for unit in unitlist:
#         for digit in '123456789':
#             places = [box for box in unit if digit in values[box]]
#             if len(places) == 1:
#                 values = assign_value(values, places[0], digit)
#     return values

# def get_solved_values(values):
#     return [box for box in values.keys() if len(values[box]) == 1]

# def reduce_puzzle(values):
#     stalled = False
#     while not stalled:
#         solved_values_before = get_solved_values(values)
#         values = eliminate(values)
#         values = only_choice(values)
#         values = naked_twins(values)
#         solved_values_after = get_solved_values(values)
#         stalled = solved_values_after == solved_values_before
#         if len([box for box in values.keys() if len(values[box]) == 0]):
#             return False
#     return values

# def search(values):
#     values = reduce_puzzle(values)
#     if values == False:
#         return False
#     if all(len(values[box]) == 1 for box in boxes):
#         return values
#     n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
#     for possible_value in values[s]:
#         new_values = values.copy()
#         new_values = assign_value(new_values, s, possible_value)
#         solved_puzzle = search(new_values)
#         if solved_puzzle:
#             return solved_puzzle

# def solve(grid):
#     """
#     Find the solution to a Sudoku grid.
#     Args:
#         grid(string): a string representing a sudoku grid.
#             Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
#     Returns:
#         The dictionary representation of the final sudoku grid. False if no solution exists.
#     """
#     values = grid_values(grid)
#     return search(values)


# def sudoku(puzzle):
#     """return the solved puzzle as a 2d array of 9 x 9"""
#     a = [item for row in puzzle for item in row]
#     a = "".join([str(x) if x != 0 else '.' for x in a])
#     return display(solve(a))
