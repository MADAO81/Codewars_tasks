# White or Black?
# Complete the function that returns the color of the given square on a normal, 8x8 chess board:
#     Examples
# 'a', 8  ==>  "white"
# 'b', 2  ==>  "black"
# 'f', 5  ==>  "white"

def square_color(file, rank):
    if (ord(file)+ rank) % 2 == 0:
        return "black"
    else:
        return "white"
        
        
# def square_color(file, rank):
#     black_squares = [("a", 1), ("a", 3), ("a", 5), ("a", 7), ("b", 2), ("b", 4), ("b", 6), ("b", 8), ("c", 1), ("c", 3), ("c", 5), ("c", 7), ("d", 2), ("d", 4), ("d", 6), ("d", 8), ("e", 1), ("e", 3), ("e", 5), ("e", 7), ("f", 2), ("f", 4), ("f", 6), ("f", 8), ("g", 1), ("g", 3), ("g", 5), ("g", 7), ("h", 2), ("h", 4), ("h", 6), ("h", 8)] 
#     white_squares = [("a", 2), ("a", 4), ("a", 6), ("a", 8), ("b", 1), ("b", 3), ("b", 5), ("b", 7), ("c", 2), ("c", 4), ("c", 6), ("c", 8), ("d", 1), ("d", 3), ("d", 5), ("d", 7), ("e", 2), ("e", 4), ("e", 6), ("e", 8), ("f", 1), ("f", 3), ("f", 5), ("f", 7), ("g", 2), ("g", 4), ("g", 6), ("g", 8), ("h", 1), ("h", 3), ("h", 5), ("h", 7)]
    
#     if (file, rank) in black_squares:
#         return "black"
#     else:
#         return "white"
