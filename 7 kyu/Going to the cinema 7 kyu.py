# https://www.codewars.com/kata/562f91ff6a8b77dfe900006e/train/python


# import math
# def movie(card, ticket, perc):
#     total_card = card
#     total_tickets = 0
#     i = 1
#     while math.ceil(total_card) >= total_tickets:
#         total_card += ticket *(perc**i)
#         total_tickets += ticket
#         i += 1
#     return i-1


import math 
def movie(card, ticket, perc):
    num = 0
    price_a = 0
    price_b = card
    while math.ceil(price_b) >= price_a:
        num += 1
        price_a += ticket
        price_b += ticket * (perc ** num)
    return num
