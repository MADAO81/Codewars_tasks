# https://www.codewars.com/kata/5572f7c346eb58ae9c000047/train/python

# def pattern(n):
#     return "\n".join([str(i)*i for i in range(1,n+1)])


# def pattern(n):
#     result = ''
#     for i in range(1, n + 1):
#         result += str(i) * i + '\n'
#     return result[:-1]


def pattern(n):
    return '\n'.join(str(i) * i for i in xrange(1, n + 1))
