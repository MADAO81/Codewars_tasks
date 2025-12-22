# https://www.codewars.com/kata/63efd90145e04e000f697d85/train/python


#/ᐠ｡.｡ᐟ\
# def the_intervals(intervals,numbers):
#     result = []
#     for number in numbers:
#         accepted_intervals = []
#         for a, b in intervals:
#             if a < number < b:
#                 accepted_intervals.append(f'({a};{b})')
#         if accepted_intervals:
#             result.append(f'{number} ∈ ' + ' ∩ '.join(accepted_intervals) )
#     return ' and '.join(result)


def the_intervals(intervals, numbers):
    return " and ".join(f"{v} ∈ {' ∩ '.join(l)}" for v,l in ((n, [f"({x};{y})" for x,y in intervals if x < n < y]) for n in numbers) if l)
