# https://www.codewars.com/kata/59d9ff9f7905dfeed50000b0/solutions/python

# def solve(strings : list[str]) -> list[int]:
#     def count_symmetry(word):
#         return sum(1 for i,c in enumerate(word.lower()) if i == ord(c)-ord("a"))
    
#     return [count_symmetry(word) for word in strings]


def solve(arr):
    return [ sum(c == chr(97+i) for i,c in enumerate(w[:26].lower())) for w in arr ]
