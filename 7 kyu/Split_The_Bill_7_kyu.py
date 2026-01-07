# https://www.codewars.com/kata/5641275f07335295f10000d0/train/python

# def split_the_bill(x):
#     total = sum(x.values())/float(len(x))
#     return {key:round(value - total,2) for key,value in x.items()}

def split_the_bill(x):
    diff = sum(x.values())/float(len(x))
    return {k: round(x[k]-diff, 2) for k in x}
