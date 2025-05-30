# Arrh, grabscrab!
# Pirates have notorious difficulty with enunciating. 
# They tend to blur all the letters together and scream at people.

# At long last, we need a way to unscramble what these pirates are saying.

# Write a function that will accept a jumble of letters as well as a dictionary, 
# and output a list of words that the pirate might have meant.

# For example:

# grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
# Should return ["sport", "ports"].

# Return matches in the same order as in the dictionary. Return an empty array if there are no matches.

# Good luck!

def grabscrab(said, possible_words):
    result = []
    for word in possible_words:
        if sorted(word) == sorted(said):
            result.append(word)
    return result
    
    
def grabscrab(said, possible_words):
    return [ word for word in possible_words if sorted(word) == sorted(said) ]
