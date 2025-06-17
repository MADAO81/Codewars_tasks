# [Code Golf] Dreidel dreidel
# Note: This is the code golf version of this kata -- 
# it's best to solve that one first. Everything is exactly the same here: 
# the input, the task, the tests, and the expected output (see details below). 
# The only difference is the code size limit.

# Your code can be maximum 110 bytes long.

# Details
# Dreidel is a gambling game. A dreidel has four sides:

# Nun - nothing happens
# Gimel - you take the pot!
# Hei - you take half the pot (rounded down)
# Shin - you put a piece into the pot
# Complete the function that receives an array of dreidel rolls, the number of coins in your account,
# and the number of coins in the pot; the input will always be valid (non-negative integers). Return the number of coins left
# in your account after the last roll. Note: you can have a negative amount at the end of the game.

from math import floor

def gamble(rolls, my_coins, pot):
    for roll in rolls:
        half = floor(pot / 2)
        if roll == "Nun":
            pass
        elif roll == "Gimel":
            my_coins += pot
            pot = 0
        elif roll == "Hei":
            my_coins += half
            pot -= half
        elif roll == "Shin":
            my_coins -= 1
            pot += 1
    return my_coins
    
    
# gamble=lambda r,a,p:a+p-[p:=p-[p>>ord(r[0])-71,-1][r>'R']for r in r][-1]
