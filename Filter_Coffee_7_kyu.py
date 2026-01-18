# https://www.codewars.com/kata/56069d0c4af7f633910000d3/train/python

# def search(budget, prices):
#     result = []
#     for price in prices:
#         if price <= budget:
#             result.append(price)
#     result.sort() 
#     return ",".join(str(n) for n in result)


# def search(budget, prices):
#     return ",".join(map(str, sorted([n for n in prices if n <= budget])))


def search(budget, prices):
    return ','.join(str(a) for a in sorted(prices) if a <= budget)
