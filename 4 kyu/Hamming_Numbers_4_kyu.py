# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python

# def hamming(n):
#     bag = {1}
#     for _ in range(n - 1):
#         head = min(bag)
#         bag.remove(head)
#         bag |= {head*2, head*3, head*5}
#     return min(bag)



def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]
