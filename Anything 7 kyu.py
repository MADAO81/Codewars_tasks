# What is the answer to life the universe and everything

# Create a function that will make anything true

#     anything({}) != [],          'True'
#     anything('Hello') < 'World', 'True'
#     anything(80) > 81,           'True'
#     anything(re) >= re,          'True'
#     anything(re) <= math,        'True'
#     anything(5) == ord,          'True'


def anything(thing):
    """
    The "anything" function returns an object that has overloaded magic comparison methods:
        __lt__(self, other)
        __le__(self, other)
        __eq__(self, other)
        __ne__(self, other)
        __gt__(self, other)
        __ge__(self, other)
    Due to polymorphism, these methods accept objects of any type,
    because the result of their operation is independent and is always True.
    Therefore, it does not matter what we pass to the function anything,
    because it will always return an object for which the comparison operations will give
    the result True.
    """
    class ComparisonAlwaysTrue:
        def __gt__(self, other):
            return True

        def __lt__(self, other):
            return True

        def __ge__(self, other):
            return True

        def __le__(self, other):
            return True

        def __eq__(self, other):
            return True

        def __ne__(self, other):
            return True

    return ComparisonAlwaysTrue()
