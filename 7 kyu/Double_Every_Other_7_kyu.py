# https://www.codewars.com/kata/5809c661f15835266900010a/train/python

# def double_every_other(lst):
#     x = []
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             x.append(lst[i] * 2)
#         else:
#             x.append(lst[i])
#     return x


def double_every_other(lst):
    return [i if index % 2 == 0 else i*2 for index,i in enumerate(lst)]
