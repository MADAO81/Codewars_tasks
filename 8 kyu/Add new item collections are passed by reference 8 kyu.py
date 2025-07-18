# Add new item (collections are passed by reference)
# Add an item to the list:
# AddExtra method adds a new item to the list and returns the list. The new item can be any object, and it does not matter. (lets say you add an integer value, like 13)
# In our test case we check to assure that the returned list has one more item than the input list. However the method needs some modification to pass this test.
# P.S. You have to create a new list and add a new item to that. 
# (This Kata is originally designed for C# language and it shows that adding a new item to the input list is not going to work, 
# even though the parameter is passed by value, but the value is poining to the reference of list and any change on parameter will be seen by caller)

def add_extra(list_of_numbers):
    new_list = list_of_numbers[:]
    new_list.append(13)
    return new_list

# def AddExtra(listOfNumbers):
#     return listOfNumbers + [13]
