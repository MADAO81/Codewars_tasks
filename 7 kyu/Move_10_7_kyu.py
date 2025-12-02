# https://www.codewars.com/kata/57cf50a7eca2603de0000090/train/python

# def move_ten(st):
#     new_str = ''
#     for i in range(len(st)):
#         val = ord(st[i]) + 10
#         if val > 122:
#             new_str += chr(val-26)
#         else:
#             new_str += chr(val)
#     return new_str


# from string import ascii_lowercase as al

# tbl = str.maketrans(al, al[10:] + al[:10])
# def move_ten(st):
#     return st.translate(tbl)


def move_ten(st):
    return ''.join(chr(ord(i)+10) if i<'q' else chr(ord(i)-16) for i in st)
