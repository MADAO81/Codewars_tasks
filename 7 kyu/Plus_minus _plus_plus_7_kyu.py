# https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca/train/python

# def catch_sign_change(lst):
#     changes = sum((x>=0)!=(y>=0) for x,y in zip(lst,lst[1:]))
#     return changes

def catch_sign_change(lst):
    count = 0
    for i in range(1,len(lst)):
        if lst[i] < 0 and lst[i-1] >= 0:count += 1
        if lst[i] >= 0 and lst[i-1] < 0:count += 1
    return count
