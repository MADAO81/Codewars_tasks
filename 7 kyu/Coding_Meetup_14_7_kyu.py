# https://www.codewars.com/kata/583952fbc23341c7180002fd/train/python

# def order_food(lst): 
#     result = {}
#     for person in lst:
#         if person['meal'] in result:
#             result[person['meal']] +=1
#         else:
#             result[person['meal']] = 1
#     return result


from collections import Counter

def order_food(lst): 
    return Counter(dev['meal'] for dev in lst)
