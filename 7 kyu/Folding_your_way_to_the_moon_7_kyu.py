# https://www.codewars.com/kata/58f0ba42e89aa6158400000e/train/python


def fold_to(distance):
    thickness = 0.0001
    result = 0
    if distance < 0:
        return None
    while thickness < distance:
        result +=1
        thickness *=2
    return result
