# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python


# def triangle(row):
#     if len(row) == 1:
#         return row
#     else:
#         temp = ''
#         for i in range(len(row)-1):
#             if i == len(row):
#                 return row
#             elif row[i] == row[i+1]:
#                 temp = temp + row[i]
#             elif row[i] in "BG" and row[i+1] in "BG":
#                 temp = temp + "R"
#             elif row[i] in "RG" and row[i+1] in "RG":
#                 temp = temp + "B"
#             elif row[i] in "BR" and row[i+1] in "BR":
#                 temp = temp + "G"
#     return triangle(temp)




# def triangle(row):
#     dicts = {'GG':'G', 'BB':'B', 'RR':'R', 'BR':'G', 'BG':'R', 'GB':'R', 'GR':'B', 'RG':'B', 'RB':'G'}
#     if len(row) > 2:
#         s = ''
#         for i in range(len(row) - 1):
#         	s = s + dicts[row[i:i + 2]]
#         row = s
#         return triangle(row)
#     elif len(row) > 1:
#         return dicts[row]
#     else:
#         return row



COLORS = set("RGB")

def triangle(row):
    while len(row)>1:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row


