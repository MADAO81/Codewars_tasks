# https://www.codewars.com/kata/58356a94f8358058f30004b5/train/python

# def fly_by(lamps, drone):
#     return lamps.replace("x","o", drone.index("T")+1)


# def fly_by(lamps, drone):
#     return lamps.replace('x', 'o', drone.count('=') + 1)


def fly_by(lamps, drone):
    return lamps.replace('x', 'o', len(drone))
