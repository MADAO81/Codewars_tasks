# https://www.codewars.com/kata/59f7fc109f0e86d705000043/train/python

# def divisible_by_three(st): 
#     while len(st) != 1:
#         st = str(sum(int(n) for n in st))
#     return int(st) in [0, 3, 6, 9]

def divisible_by_three(st): 
    if len(st) == 1:
        return st in '369'
    return divisible_by_three(str(sum(map(int, st))))
