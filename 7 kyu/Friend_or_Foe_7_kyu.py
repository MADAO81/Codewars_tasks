# Friend or Foe?
# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []
# Input strings will only contain letters.
# Note: keep the original order of the names in the output.


# def friend(x):
#     friend_list = []
#     for person in x:
#         if len(person) == 4:
#             friend_list.append(person)
#     return friend_list        
    
    
def friend(x):
    return [f for f in x if len(f) == 4]
