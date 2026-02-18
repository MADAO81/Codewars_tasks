# Create a function add(n)/Add(n) which returns a function that always adds n to any number

# Note for Java: the return type and methods have not been provided to make it a bit more challenging.

# add_one = add(1)
# add_one(3)  # 4

# add_three = add(3)
# add_three(3) # 6


# from typing import Callable

# def add(n: int) -> Callable:
#     def add_something(i):
#         return n+i
#     return add_something


def add(n):
    return lambda x: x + n
