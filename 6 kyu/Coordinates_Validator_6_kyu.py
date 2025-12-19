# https://www.codewars.com/kata/5269452810342858ec000951/train/python

# def is_valid_coordinates(coordinates):
#     if ', ' not in coordinates:
#         return False
#     coord1, coord2 = coordinates.split(', ')
    
#     for char in coord1 + coord2:
#         if char not in ['0','1','2','3','4','5','6','7','8','9','.','-','_']:
#             print(char)
#             return False
#     try:
#         return True if (abs(float(coord1)) <= 90 and abs(float(coord2)) <= 180) else False
#     except:
#         return False


def is_valid_coordinates(coordinates):
    try:
        lat, lng = [abs(float(c)) for c in coordinates.split(',') if 'e' not in c]
    except ValueError:
        return False

    return lat <= 90 and lng <= 180
