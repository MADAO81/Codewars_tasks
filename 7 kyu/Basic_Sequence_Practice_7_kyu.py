# https://www.codewars.com/kata/5436f26c4e3d6c40e5000282/train/python

# def sum_of_n(n):
#     if n<0:
#         return sorted([sum(x for x in range(i,1)) for i in range(n,1)], reverse = True)
#     else:
#         return [sum([x for x in range(i+1)]) for i in range(n+1)]


# def sum_of_n(n):
#     result = [0]
#     sign = 1
#     if n < 0: 
#       sign = -1
#     for number in range(1, abs(n) + 1):
#         output.append(sign * (number + abs(result[number - 1])))
#     return result


def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]
