# https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/python

# from math import ceil
# def new_avg(arr, newavg):
#     dons = len(arr)
#     total_dons = dons + 1
#     result = ceil((total_dons * newavg) - sum(arr))
#     if result >0:
#         return result
#     else:
#         raise ValueError


from math import ceil

def new_avg(arr, newavg):
    # calculate the required amount
    required = ceil(newavg * (len(arr) + 1) - sum(arr))
    # throw an error if non-positive
    assert required > 0
    # otherwise return result
    return required
