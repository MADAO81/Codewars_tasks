# https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7/train/python

# def squares_needed(grains):
#     count = 0
#     grain_total = 1
#     if grains == 0:
#         return 0
#     else:
#         while grain_total <= grains:
#             count +=1
#             grain_total = grain_total * 2
#         return count


# def squares_needed(grains):
#     if grains < 1:
#         return 0
#     else:
#         return 1 + squares_needed(grains // 2)


def squares_needed(grains):
    return grains.bit_length()
