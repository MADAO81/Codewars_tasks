# Given a non-negative integer, return an array / a list of the individual digits in order.
# Examples:
# 123 => [1,2,3]
# 1 => [1]
# 8675309 => [8,6,7,5,3,0,9]

# def digitize(n):
#     result = []
#     for i in str(n):
#         result.append(int(i))
#     return result


# def digitize(n):
#     return list(map(int, str(n)))


def digitize(n):
    return [int(d) for d in str(n)]
