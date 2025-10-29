# https://www.codewars.com/kata/5865cff66b5699883f0001aa/train/python

def to_time(seconds):
    return f'{seconds//3600} hour(s) and {(seconds//60)%60} minute(s)'
