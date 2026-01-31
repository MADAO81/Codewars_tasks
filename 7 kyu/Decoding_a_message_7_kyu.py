# Decoding a message
# You have managed to intercept an important message and you are trying to read it.
# You realise that the message has been encoded and can be decoded by switching each letter
# with a corresponding letter.
# You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.
# For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc


# import string
# def decode(message):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     trans = str.maketrans(alphabet, alphabet[::-1], '')
#     return message.lower().translate(trans)


from string import ascii_lowercase as alphabet
def decode(message):
    return message.translate(str.maketrans(alphabet, alphabet[::-1]))
