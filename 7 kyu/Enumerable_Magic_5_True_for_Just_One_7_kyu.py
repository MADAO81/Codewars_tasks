# https://www.codewars.com/kata/54599705cbae2aa60b0011a4/train/python

# def one(xs, f): 
#     return sum([1 for tmp in xs if f(tmp)]) == 1


# def one(sq, fun): 
#     return sum(fun(x) for x in sq)==1


def one(sq, fun): 
    return sum(map(fun,sq))==1
