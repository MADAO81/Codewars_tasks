# https://www.codewars.com/kata/586ec0b8d098206cce001141/train/python

# def inverse_slice(items, a, b):
#     return [v for idx,v in enumerate(items) if not a<= idx < b ]


# def inverse_slice(items, a, b):
#     del items[a:b]
#     return items

# def inverse_slice(items, a, b):
#     part1 = items[:a]
#     part2 = items[b:]
#     return (part1+part2)


def inverse_slice(items, a, b):
    return items[:a] + items[b:]
