# https://www.codewars.com/kata/609eee71109f860006c377d1/train/python

# def last_survivor(letters, coords): 
#     chars = list(letters)
#     result = ''
#     while coords:
#         chars.pop(coords[0])
#         coords.pop(0)
#     for ch in chars:
#         result +=ch
#     return result


# def last_survivor(letters, coords): 
#     letters = list(letters)
#     for coord in coords:
#         letters.pop(coord)
#     return letters[0]



def last_survivor(letters, coords):
    for x in coords:
        letters = letters[0:x] + letters[x+1:]
    return letters
