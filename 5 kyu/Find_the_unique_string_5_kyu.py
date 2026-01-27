# https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3/train/python


# from collections import Counter
# def find_uniq(arr):
#     new_arr = []
#     for element in arr:
#         new_arr.append(''.join(sorted(list(set(element.lower())))))
#     unique = Counter(new_arr).most_common()
#     for i,el in enumerate(new_arr):
#         if unique[1][0] in el:
#             return arr[i]



# def find_uniq(arr):
#     if set(arr[0].lower()) == set(arr[1].lower()):
#         majority_set = set(arr[0].lower())
#     elif set(arr[0].lower()) == set(arr[2].lower()):
#         majority_set = set(arr[0].lower())
#     else:
#         majority_set = set(arr[1].lower())
    
#     for string in arr:
#         if set(string.lower()) != majority_set:
#             return string



from collections import defaultdict

def find_uniq(a):
    d = {}
    c = defaultdict(int)
    for e in a:
        t = frozenset(e.strip().lower())
        d[t] = e
        c[t] += 1
    
    return d[next(filter(lambda k: c[k] == 1, c))]
