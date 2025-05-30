# 80's Kids #2: Help ALF Find His Spaceship

# Late last night in the Tanner household, ALF was repairing his spaceship so he might get back to Melmac.
# Unfortunately for him, he forgot to put on the parking brake, and the spaceship took off during repair. Now it's hovering in space.
# ALF has the technology to bring the spaceship home if he can lock on to its location.
# Given a map:

# ..........
# ..........
# ..........
# .......X..
# ..........
# ..........
# The map will be given in the form of a string with \n separating new lines. 
# The bottom left of the map is [0, 0]. X is ALF's spaceship.

# In this example:
# findSpaceship(map) => [7, 2]
# If you cannot find the spaceship, the result should be
# "Spaceship lost forever."
# Can you help ALF?

def find_spaceship(astromap):
    if 'X' not in astromap:
        return 'Spaceship lost forever.'
    astromap = astromap.split('\n')
    for i in astromap:
        if 'X' in i:
            return [i.index('X'), len(astromap) - (astromap.index(i) + 1)]
            
# def find_spaceship(astromap):
#     lines = astromap.splitlines()
#     for y, line in enumerate(lines):
#         x = line.find('X')
#         if x != -1:
#             return [x, len(lines) - 1 - y]
#     return 'Spaceship lost forever.'
