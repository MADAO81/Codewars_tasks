# https://www.codewars.com/kata/525d9b1a037b7a9da7000905/train/python

def search_names(logins):
    return list(filter(lambda a: a[0].endswith('_'), logins))
