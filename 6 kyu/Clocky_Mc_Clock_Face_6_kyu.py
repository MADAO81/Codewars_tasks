# https://www.codewars.com/kata/59752e1f064d1261cb0000ec/train/python

# import math

# def what_time_is_it(angle):
#     hour = math.floor(angle * 2 / 60)
#     minute = math.floor(angle *2 % 60)
#     if hour == 0:
#         hour = "12"
#     elif hour < 10:
#         hour = "0" + str(hour)
#     if minute < 10:
#         minute = "0" + str(minute)
#     return f"{hour}:{minute}"


# def what_time_is_it(angle):
#     angle %= 360
#     h, m = divmod(angle, 30)
#     return '{:02}:{:02}'.format(int(h or 12), int(m * 2))


def what_time_is_it(angle):
    hr = int(angle // 30)
    mn = int((angle % 30) * 2)
    if hr == 0:
        hr = 12
    return '{:02d}:{:02d}'.format(hr, mn)
