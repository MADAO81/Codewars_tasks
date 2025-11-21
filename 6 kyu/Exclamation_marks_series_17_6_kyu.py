# https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python

# def balance(left, right):
#     left_sum = 0
#     right_sum = 0
#     for el in left:
#         if el == "":
#             left_sum +=0
#         elif el == "!":
#             left_sum += 2
#         elif el == "?":
#             left_sum += 3
#     for el in right:
#         if el == "":
#             right_sum +=0
#         elif el == "!":
#             right_sum += 2
#         elif el == "?":
#             right_sum += 3
#     if right_sum == left_sum:
#         return "Balance"
#     elif right_sum > left_sum:
#         return "Right"
#     else:
#         return "Left"


def balance(left, right):
  left_count = left.count("!")*2 + left.count("?")*3
  right_count = right.count("!")*2 + right.count("?")*3

  if(left_count > right_count):
    return "Left"
  elif(right_count>left_count):
    return "Right"
  else:
    return "Balance"
