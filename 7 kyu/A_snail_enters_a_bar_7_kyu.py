# https://www.codewars.com/kata/66cdc6ab9e7a9f009e0ca8f6/train/python

# def can_snail_reach_end(length, speed, length_increases):
#     for i in range(1,365+1):
#         length -= speed
#         length += length_increases

#     return False if length > 0 else True


def can_snail_reach_end(x, y, z):
    return (y-z)*525600 >= x
