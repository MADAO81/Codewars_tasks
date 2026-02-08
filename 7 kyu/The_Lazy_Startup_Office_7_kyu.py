# https://www.codewars.com/kata/578fdcfc75ffd1112c0001a1/train/python


# def bin_rota(arr):
#     result = []
#     for rows, columns in enumerate(arr):
#         if rows%2 == 0:
#             for i in columns:
#                 result.append(i)
#         else:
#             for i in columns[::-1]:
#                 result.append(i)
#     return result


def bin_rota(arr):
    return [name for i,row in enumerate(arr) for name in (reversed(row) if i&1 else row)]
