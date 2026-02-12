# https://www.codewars.com/kata/571c1e847beb0a8f8900153d/train/python

# def rake_garden(garden):
#     clear_garden = garden.split()
#     result = []
#     for element in clear_garden:
#         if element not in ['rock', 'gravel']:
#             element = 'gravel'
#         result.append(element)
#     return ' '.join(result)



# def rake_garden(garden):
#     return " ".join(w if w == "rock" else "gravel" for w in garden.split())



VALID = {'gravel', 'rock'}


def rake_garden(garden):
    return ' '.join(a if a in VALID else 'gravel' for a in garden.split())
