# You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

# For each word:

# the second and the last letter is switched (e.g. Hello becomes Holle)
# the first letter is replaced by its character code (e.g. H becomes 72)
# there are no special characters used, only letters and spaces
# words are separated by a single space
# there are no leading or trailing spaces
# Examples

# '72olle 103doo 100ya' --> 'Hello good day'
# '82yade 115te 103o'   --> 'Ready set go'

def decipher_word(word):
    i = sum(map(str.isdigit, word))
    decoded = chr(int(word[:i]))
    if len(word) > i + 1:
        decoded += word[-1]
    if len(word) > i:
        decoded += word[i+1:-1] + word[i:i+1]
    return decoded

def decipher_this(string):
    return ' '.join(map(decipher_word, string.split()))
