# https://www.codewars.com/kata/63f96036b15a210058300ca9/train/python

# def second_symbol(s, symbol):
#     counter=0
#     for i in range(len(s)):
#         if s[i]==symbol:
#             counter+=1
#         if counter==2:
#             return i
#     return -1


# def second_symbol(s, c):
#     if not c or s.count(c) < 2:
#         return -1
#     return s.index(c, s.index(c) + 1)
  



def second_symbol(s, symbol):
    return s.find(symbol, s.find(symbol)+1)
