# Dashatize it
# Given an integer, return a string with dash '-' marks before
# and after each odd digit, but do not begin or end the string with a dash mark.

# Ex:

# 274 -> '2-7-4'
# 6815 -> '68-1-5'

def dashatize(n):
    n = str(n)
    odds = ["1","3","5","7","9"]
    for i in odds:
        n = n.replace(i,"-" + i + "-")
    n = n.replace("--","-")
    n = n.strip("-")
    return n
    
# import re
# def dashatize(num):
#     try:
#         return ''.join(['-'+i+'-' if int(i)%2 else i for i in str(abs(num))]).replace('--','-').strip('-')
#     except:
#         return 'None'


# def dashatize(num):
#     num_str = str(num)
#     for i in ['1','3','5','7','9']:
#         num_str = num_str.replace(i,'-' + i + '-')
#     return num_str.strip('-').replace('--','-')
