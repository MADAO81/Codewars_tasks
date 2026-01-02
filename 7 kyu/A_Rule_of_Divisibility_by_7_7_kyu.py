# https://www.codewars.com/kata/55e6f5e58f7817808e00002e/train/python

# def seven(m):
#     steps = 0
#     while len(str(m)) > 2:
#         m = int(str(m)[:-1]) - 2*int(str(m)[-1])
#         steps +=1
#         if m%7 == 0 and len(str(m)) <= 2:
#             break
#     return (m,steps)



def seven(m, step = 0):
    if m < 100: 
        return (m, step)
    x, y, step = m // 10, m % 10, step + 1
    result = x - 2 * y
    return seven(result, step)
