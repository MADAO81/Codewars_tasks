# https://www.codewars.com/kata/58291fea7ff3f640980000f9

# def all_continents(lst): 
#     return len(set([el['continent'] for el in lst])) == 5

def all_continents(lst): 
    return set(['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']) == set([el['continent'] for el in lst])
