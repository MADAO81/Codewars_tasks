# https://www.codewars.com/kata/582dace555a1f4d859000058/train/python

# def find_admin(lst, lang): 
#     return [i for i in lst if i['language'] == lang and i['githubAdmin'] == 'yes']


def find_admin(lst, lang): 
    return list(filter(lambda x: x['language']==lang and x['githubAdmin']=='yes', lst))
