# https://www.codewars.com/kata/691ca4c58c5f7e662d508d31/train/python

def find_saddle_points(matrix):
    columns = list(zip(*matrix))
    min_row = list(map(min, matrix))
    max_col = list(map(max, columns))
    
    return [ (row, col)
            for row in range(len(matrix))
                for col in range(len(columns))
                    if min_row[row] == max_col[col]
        ]
