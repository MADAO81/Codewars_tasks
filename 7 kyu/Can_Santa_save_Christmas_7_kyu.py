# https://www.codewars.com/kata/5857e8bb9948644aa1000246/train/python

# def determine_time(arr):
#     #have fun with coding ^.^
#     hh,mm,ss = 0,0,0
#     for i in arr:
#         hh += int(i.split(":")[0])
#         mm += int(i.split(":")[1])
#         ss += int(i.split(":")[2])
#     total = (hh*3600)+(mm*60)+ss
#     if 86400 < total:
#         return False
#     else:
#         return True


def determine_time(arr):
    total = 0
    
    for time in arr:
        h, m, s = map(int, time.split(":"))
        total += h*60*60 + m*60 + s
    
    return total <= 24*60*60
