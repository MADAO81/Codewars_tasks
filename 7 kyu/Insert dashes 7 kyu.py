# https://www.codewars.com/kata/55960bbb182094bc4800007b/train/python

# def insert_dash(num):
#     num = str(num)
#     odd = {1,3,5,7,9}
#     dex = {i for i, a in enumerate(num) if int(a) in odd}
#     return "".join(b+"-" if {i,i+1}.issubset(dex) else b for i,b in enumerate(num))



# def insert_dash(num):
  
#   digits = [d for d in str(num)]
  
#   for i in range(len(digits)-1):
#     if int(digits[i])%2 and int(digits[i+1])%2:
#       digits[i] = digits[i] + '-'
  
#   return ''.join(digits)



import re

def insert_dash(num):
    return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))
