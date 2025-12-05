# https://www.codewars.com/kata/5ae7e3f068e6445bc8000046/train/python

# def next_happy_year(year):
#     while True:
#         year +=1
#         if len(list(set(str(year)))) == 4:
#             return year


def next_happy_year(year):
    year += 1    
    while len(set(str(year))) != 4:
        year += 1    
    return year
