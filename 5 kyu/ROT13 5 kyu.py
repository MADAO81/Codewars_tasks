# How can you tell an extrovert from an introvert at NSA?
# Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
# According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

# For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

# Test examples:

# "EBG13 rknzcyr." -> "ROT13 example."

# "This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

# def rot13(message):
#     import codecs
#     return codecs.encode(message, 'rot_13')

# def rot13(message):
#     cipher_table = {}
#     for ch in range(0,26):
#         cipher_table[chr(ch + ord("A"))] = chr(((ch + 13) % 26) + ord("A"))
#         cipher_table[chr(ch + ord("a"))] = chr(((ch + 13) % 26) + ord("a"))
#     return "".join([cipher_table[char] if char in cipher_table else char for char in message])

# import string

# def rot13(message):
# 	first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#    	trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
# 	return message.translate(string.maketrans(first, trance)) 

def rot13(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)

