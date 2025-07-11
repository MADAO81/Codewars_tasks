# Surface Area and Volume of a Box
# Write a function that returns the total surface area and volume of a box.

# The given input will be three positive non-zero integers: width, height, and depth.

# The output will be language dependant, so please check sample tests for the corresponding data type, (list, tuple, struct, query, et cetera).

def get_size(w,h,d):
    return [2*(w*h + h*d + w*d), w*h*d]
