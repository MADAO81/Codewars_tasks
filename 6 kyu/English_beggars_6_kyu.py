# https://www.codewars.com/kata/59590976838112bfea0000fa/train/python

# def beggars(values, n):
#     result = []
#     for i in range(n):
#         inds = list(range(i,len(values),n))
#         total = 0
#         for index in inds:
#             total += values[index]
#         result.append(total)
#     return result


def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]
