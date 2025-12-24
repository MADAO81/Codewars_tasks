# https://www.codewars.com/kata/582887f7d04efdaae3000090/train/python

# def find_senior(lst): 
#     mage = max(a['age'] for a in lst)
#     return [a for a in lst if a['age']==mage]

def find_senior(lst): 
    return [i for i in lst if i['age'] == max(i['age'] for i in lst)]
