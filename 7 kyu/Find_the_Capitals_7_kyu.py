# https://www.codewars.com/kata/53573877d5493b4d6e00050c/solutions/python


# def capital(capitals): 
#     result = []
#     for i in capitals:
#         if 'country' in i:
#             result.append(f"The capital of {i['country']} is {i['capital']}")
#         else:
#             result.append(f"The capital of {i['state']} is {i['capital']}")
#     return result


def capital(capitals):
    return [f"The capital of {c.get('state') or c['country']} is {c['capital']}" for c in capitals]
