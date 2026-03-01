# Description:
# Encrypt this!

# You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

# Your message is a string containing space separated words.
# You need to encrypt each word in the message using the following rules:
# The first letter must be converted to its ASCII code.
# The second letter must be switched with the last letter
# Keepin' it simple: There are no special characters in the input.

# def encrypt_this(text):
#     encrypted = ""
#     text = text.split()
#     for word in text:
#         first_ch,word = str(ord(word[:1])), word[1:]
#         second_ch,word = word[:1],word[1:]
#         last_ch,word = word[-1:],word[:-1]
#         encrypted += first_ch + last_ch + word + second_ch + " "
#     return encrypted[:-1]


def encrypt_this(text):
    result = []
    
    for word in text.split():
        # turn word into a list
        word = list(word)
        
        # replace first letter with ascii code
        word[0] = str(ord(word[0]))
        
        # switch 2nd and last letters
        if len(word) > 2:
            word[1], word[-1] = word[-1], word[1]
        
        # add to results
        result.append(''.join(word))
    
    return ' '.join(result)
