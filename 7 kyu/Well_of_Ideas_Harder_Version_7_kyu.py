# https://www.codewars.com/kata/57f22b0f1b5432ff09001cab/train/python

def well(arr):
    good_ideas = str(arr).lower().count('good')
    return 'I smell a series!' if (good_ideas > 2) else 'Fail!' if not(good_ideas) else 'Publish!'
