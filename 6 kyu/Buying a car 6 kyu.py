# https://www.codewars.com/kata/554a44516729e4d80b000012/train/python

def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    month_to_buy = 0
    savings = 0
    
    while start_price_old + savings < start_price_new:
        month_to_buy += 1
        savings += saving_per_month
        if month_to_buy % 2 == 0:
            percent_loss_by_month += 0.5
        start_price_old *= (100-percent_loss_by_month)/100
        start_price_new *= (100-percent_loss_by_month)/100
    
    money_left = round(start_price_old + savings - start_price_new)
    return [month_to_buy,money_left]

