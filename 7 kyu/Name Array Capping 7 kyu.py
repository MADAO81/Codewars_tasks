# Name Array Capping
# Create a function that accepts an array of names, and returns 
# an array of each name with its first letter capitalized and the remainder in lowercase.

# Examples
# ['jo', 'nelson', 'jurie'] -->  ['Jo', 'Nelson', 'Jurie']
# ['KARLY', 'DANIEL', 'KELSEY'] --> ['Karly', 'Daniel', 'Kelsey']

def cap_me(arr):
    result = []
    for ch in arr:
        if ch == "":
            result.append(ch)
        else:
            result.append(ch[0].upper()+ch[1:].lower())
    return result
    
# return [name.capitalize() for name in arr]
