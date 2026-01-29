# Problem / Lore
# William is a great beverage merchant from the Middle Ages. Lately, he has noticed that the space in his barrels warehouse is being misused. As he sells different types of beverages, 
# it is common for barrels to be removed and inserted in random positions, leaving several empty spaces of different sizes. So he decided that it was not worth redistributing 
# the barrels and that new barrels should be placed contiguously and in the smallest available space they can fit in.

# Challenge Description
# Your task is to create a function that will help William better manage his warehouse, your function receives two parameters:

# The first is a array that represents a warehouse of barrels; each character '0' represents a barrel, and an empty string '' represents an available space.
# The second parameter is a array of '0', which are the new barrels to be inserted (they must be inserted together).
# You must find the first smallest available space where the new barrels fit and place them there from left to right. Return the array of barrels with the new barrels inserted.

# Examples (input -> output)
# ['0','','','0','','','','0'], ['0','0'] -> ['0','0','0','0','','','','0']

# ['0','0','','','0','','','','0'], ['0'] -> ['0','0','0','','0','','','','0']
# More examples in test cases

# Notes
# The priority is that the space is as small as possible, so first you must find the smallest spaces that fit, and if there is a tie, place them in the leftmost space.
# When placed, the barrels must be positioned from left to right in the available space.
# If there isn't enough space, return the warehouse unchanged.
# Good luck!

def count_empty_space(warehouse, target): 
    # count the number of consecutive items equal to target in the warehouse list.
    count = 0
    max_count = 0
    
    for i, element in enumerate(warehouse):
        if element == target:
            count += 1
            max_count = max(max_count, count) # update max quantity
        else:
            count = 0 # reset the counter in case of a mismatch
    return max_count

def insert_barrels(warehouse, barrels):
    space = []
    temp = []
    empty_space_row = count_empty_space(warehouse, "")
    if int(empty_space_row) < len(barrels):
        return warehouse
    else:
        for n,x in enumerate(warehouse):
            if x == "":
                temp.append(n)
            if x != "":
                if len(temp) >= len(barrels):
                    space.append(temp)
                temp = []
        if len(temp) >= len(barrels):
            space.append(temp)
        if space:
            for n, x in enumerate(min(space, key=len)):
                if n == len(barrels):
                    break
                warehouse[x]
