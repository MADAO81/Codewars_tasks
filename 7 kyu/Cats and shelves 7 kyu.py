# https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/python


# def solution(start, finish):
#     return sum(divmod(finish-start, 3))


def solution(start, finish):  
    return (finish-start) // 3 + (finish-start) % 3
