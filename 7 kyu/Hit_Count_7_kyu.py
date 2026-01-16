# https://www.codewars.com/kata/57b6f850a6fdc76523001162/train/python

# def counter_effect(hit_count):
#     result = []
#     for digit in hit_count:
#         num = int(digit)
#         item = []
#         for i in range(0, num + 1):
#             item.append(i)
#         result.append(item)
#     return result


# def counter_effect(hit):
#     b = []
#     for i in str(hit):
#         a = []
#         for k in range(int(i)+1):
#             a.append(k)
#         b.append(a)
#     return b


def counter_effect(n):
    return [list(range(int(x)+1)) for x in n]
