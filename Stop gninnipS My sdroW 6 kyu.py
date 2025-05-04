# Stop gninnipS My sdroW!
# Write a function that takes in a string of one or more words, 
# and returns the same string, but with all words that have five or more 
# letters reversed (Just like the name of this Kata). Strings passed in 
# will consist of only letters and spaces. Spaces will be included only 
# when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(sentence):
    result = []
    for word in sentence.split(): 
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)

# def spin_words(sentence):
# return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
