# https://www.codewars.com/kata/5571f712ddf00b54420000ee/train/python


# CHANGES = (('Quarters', 25),
#            ('Dimes',    10),
#            ('Nickels',   5),
#            ('Pennies',   1))

# def loose_change(cents):
#     cents, changed = max(0, int(cents)), {}
#     for what,value in CHANGES:
#         n,cents = divmod(cents,value)
#         changed[what] = n
#     return changed



# def loose_change(cents):
#     c = max(int(cents), 0)
#     return {'Quarters': c/25, 'Dimes': c%25/10, 'Nickels': c%25%10/5, 'Pennies': c%5}


import math

def loose_change(cents):
    if cents < 0:
        cents = 0
    cents = int(cents)
    
    change = {}

    change['Quarters'] = cents // 25
    cents = cents % 25

    change['Dimes'] = cents // 10
    cents = cents % 10

    change['Nickels'] = cents // 5
    cents = cents % 5
    
    change['Pennies'] = cents
    
    return change
