# https://www.codewars.com/kata/5a9e86705ee396d6be000091/train/python


from collections import Counter

def check_three_and_two(array):
    counts = Counter(array).values()
    if all(x in counts for x in[3,2]):
        return True
    return False
    
