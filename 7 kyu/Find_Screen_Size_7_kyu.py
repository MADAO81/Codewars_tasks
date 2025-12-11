# https://www.codewars.com/kata/5bbd279c8f8bbd5ee500000f/train/python

# import math 

# def find_screen_height(width, ratio): 
#     [w,h] = ratio.split(':')
#     w = int(w)
#     h = int(h)
#     height = math.trunc(width / w*h)
#     return str(width) + 'x' + str(height)


def find_screen_height(width, ratio): 
    a, b = map(int, ratio.split(":"))
    return f"{width}x{int(width / a * b)}"
