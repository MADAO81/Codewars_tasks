# https://www.codewars.com/kata/55955a48a4e9c1a77500005a/train/python


# def greet(name):
#     if name == "" or name == None:
#         return None
#     else:
#         return f"hello {name}!"

def greet(name):
    return f"hello {name}!" if name else None
