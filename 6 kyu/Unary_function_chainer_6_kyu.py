# https://www.codewars.com/kata/54ca3e777120b56cb6000710/train/python


# def chained(functions):
#     return lambda x : chained(functions[1:])(functions[0](x)) if functions else x


def chained(functions):
    def func(arg):
        for function in functions:
            arg = function(arg)
        return arg
    return func
