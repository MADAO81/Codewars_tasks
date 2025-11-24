# https://www.codewars.com/kata/5768a693a3205e1cc100071f/train/python

# def initialize_names(name):
#     name = name.split()
#     if len(name) <= 2:
#         return " ".join(name)
#     else:
#         return f"{name[0]} {' '.join(i[0].upper() + '.' for i in name[1:len(name)-1])} {name[-1]}"


def initializeNames(name):
    names = name.split()
    names[1:-1] = map(lambda n: n[0] + '.', names[1:-1])
    return ' '.join(names)
