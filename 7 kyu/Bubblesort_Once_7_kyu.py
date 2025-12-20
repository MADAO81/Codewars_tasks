# https://www.codewars.com/kata/56b97b776ffcea598a0006f2/train/python

# def bubblesort_once(l):
#     result = l.copy()
#     for number in range(len(result)-1):
#         if result[number] > result[number+1]:
#             result[number],result[number+1] = result[number+1], result[number]
#     return result


def bubblesort_once(l):
    l = l[:]
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    return l
    
