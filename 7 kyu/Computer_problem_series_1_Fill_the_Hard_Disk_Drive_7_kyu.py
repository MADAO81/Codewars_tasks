# https://www.codewars.com/kata/5d49c93d089c6e000ff8428c/train/python

# def save(sizes, hd):
#     return len([i for i in range(len(sizes)) if sum(sizes[:i+1]) <= hd])

def save(sizes, hd): 
    for i,s in enumerate(sizes):
        if hd < s: return i
        hd -= s
    return len(sizes)
