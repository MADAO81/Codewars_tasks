# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/solutions/python


def validate_battlefield(field):
    for i in range(10):
        for j in range(10):
            if field[i][j]:
                field[i][j] = sum(1 for x in range(max(i - 1, 0), min(i + 1, 9) + 1)
                                  for y in range(max(j - 1, 0), min(j + 1, 9) + 1) if field[x][y])
    return sum(sum(row) for row in field) == 40
