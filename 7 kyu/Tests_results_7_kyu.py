# https://www.codewars.com/kata/599db0a227ca9f294b0000c8/train/python

# def test(r):
#     m = round(sum(r)/len(r), 3)
#     dic = {'h':0, 'a':0, 'l':0}
#     for i in r:
#         if i > 8: 
#             dic['h'] += 1
#         elif i > 6: 
#             dic['a'] += 1
#         else: 
#             dic['l'] += 1
#     return [m, dic, 'They did well'] if dic['a']==0 and dic['l']== 0 else [m, dic]


from statistics import mean

def test(r):
    dct = {'l': 0, 'a': 0, 'h': 0}
    for n in r: dct[ 'lah'[(n>6) + (n>8)] ] += 1
    return [round(mean(r), 3), dct] + ['They did well'] * (sum(dct.values()) == dct['h'])
