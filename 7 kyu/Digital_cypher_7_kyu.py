# https://www.codewars.com/kata/592e830e043b99888600002d/train/python

# def encode(message, key):
#         alphabet = {
#         'a': 1,'b': 2,
#         'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,'k': 11,'l': 12,'m': 13,'n': 14,'o': 15,'p': 16,
#         'q': 17,'r': 18,'s': 19,'t': 20,'u': 21,'v': 22,'w': 23,'x': 24,'y': 25,'z': 26
#         }
#         result = []
#         key_lst = str(key)
#         count = 0
#         for ch in message:
#             result.append(alphabet[ch] + int(key_lst[count]))
#             count += 1
#             if count >= len(key_lst):
#                 count = 0
#         return result


from itertools import cycle

def encode(message, key):
    return [ord(a) - 96 + int(b) for a,b in zip(message,cycle(str(key)))]
