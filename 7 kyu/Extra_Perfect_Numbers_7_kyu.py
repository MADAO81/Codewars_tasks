# https://www.codewars.com/kata/5a662a02e626c54e87000123/train/python

# def extra_perfect(n: int) -> list[int] :
#     return [i for i in range(n+1) if i%2 !=0]

def extra_perfect(n):
    return list(range(1,n+1,2))
