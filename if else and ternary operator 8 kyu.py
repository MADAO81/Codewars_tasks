# Training JS #7: if..else and ternary operator
# Task:
# Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accepts 1 parameter:
#     n, n is the number of hotdogs a customer will buy, different numbers have different prices (refer to the following table), 
#     return how much money will the customer spend to buy that number of hotdogs.

# number of hotdogs	price per unit (cents)
# n < 5	100
# n >= 5 and n < 10	95
# n >= 10	90
# You can use if..else or ternary operator to complete it.

# When you have finished the work, click "Run Tests" to see if your code is working properly.

# In the end, click "Submit" to submit your code and pass this kata.

def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif 5 <= n <10:
        return n * 95
    else:
        return n * 90
        
# def sale_hotdogs(n):
#     return n * (100 if n < 5 else 95 if n < 10 else 90)