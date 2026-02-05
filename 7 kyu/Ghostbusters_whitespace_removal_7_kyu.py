# https://www.codewars.com/kata/5668e3800636a6cd6a000018/train/python

# def ghostbusters(building):
#     if building == building.replace(" ",""):
#         return "You just wanted my autograph didn't you?"
#     else:
#         return building.replace(" ","")


message = "You just wanted my autograph didn't you?"

def ghostbusters(building):
    return building.replace(' ', '') if ' ' in building else message
