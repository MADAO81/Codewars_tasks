# https://www.codewars.com/kata/5a0b4dc2ffe75f72f70000ef/train/python

# def find_children(santas_list, children):
#     return sorted(set(santas_list) & set(children))

# def find_children(a, b):
#     return sorted(set(a) & set(b))

def find_children(santas_list, children):
    return sorted(list(set(santas_list).intersection(children)))
