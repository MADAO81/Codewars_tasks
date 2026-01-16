# https://www.codewars.com/kata/59557b2a6e595316ab000046/train/python

# def convert_hash_to_array(dct):
#     result = []
#     for el in list(dct.items()):
#         result.append(list(el))
#     return result


# def convert_hash_to_array(dct):
#     return sorted(list(item) for item in dct.items())


# def convert_hash_to_array(hash):
#     return [[k, hash[k]] for k in sorted(hash)]


def convert_hash_to_array(hash):
    return sorted(map(list, hash.items()))

