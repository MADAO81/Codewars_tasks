# https://www.codewars.com/kata/5512e5662b34d88e44000060/train/python


# def find_missing_number(sequence):
#     try:
#         sequence = [int(n) for n in sequence.split()]
#     except ValueError:
#         return 1
#     for i, n in enumerate(sorted(sequence)):
#         if n != i + 1:
#             return i + 1
#     return 0



def find_missing_number(sequence):
    try:
        numbers = sorted([int(x) for x in sequence.split()])
        for i in range(1, len(numbers)+1):
            if i not in numbers:
                return i
    except ValueError:
        return 1
            
    return 0
