# https://www.codewars.com/kata/5af15a37de4c7f223e00012d/train/python

# def men_from_boys(arr):
#     men = []
#     boys = []
#     for i in set(arr):
#         if i%2 != 0:
#             men.append(i)
#         else:
#             boys.append(i)
#     return sorted(boys) + sorted(men,reverse = True)

def men_from_boys(arr):
    return sorted([i for i in set(arr) if i % 2 == 0]) + sorted([i for i in set(arr) if i % 2 != 0], reverse=True)
