# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ", 
#   "    ***    ", 
#   "   *****   ", 
#   "  *******  ", 
#   " ********* ", 
#   "***********"
# ]

def tower_builder(n_floors):
    tower = []
    floor = ""
    
    for ch in range(n_floors):
        brick = "*"*(ch*2 +1)
        space = " " *(n_floors - ch - 1)
        floor = space + brick + space
        tower.append(floor)
    return tower

# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
