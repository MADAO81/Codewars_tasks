# https://www.codewars.com/kata/582ba36cc1901399a70005fc/train/python


# from numpy import average

# def get_average(lst): 
#     return round(average([i['age'] for i in lst]))


def get_average(lst): 
    return round(sum(x["age"] for x in lst) / len(lst))
