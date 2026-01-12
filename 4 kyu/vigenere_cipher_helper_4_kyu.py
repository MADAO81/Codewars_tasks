# https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

# class VigenereCipher(object):
#     def __init__(self, key, alphabet):
#         self.key = key
#         self.alphabet = alphabet
    
#     def encode(self, text):
#         encrypted = []
#         alphabet = self.alphabet
#         key = self.key
#         alphabet_len = len(alphabet)
#         key_len = len(key)
#         for i, char in enumerate(text):
#                 encrypted.append(alphabet[(alphabet.index(char) + alphabet.index(
#                 key[i % key_len])) % alphabet_len] if char in alphabet else char)
#         return ''.join(encrypted)

#     def decode(self, text):
#         encrypted = []
#         key = self.key
#         key_len = len(key)
#         alphabet = self.alphabet
#         for i, char in enumerate(text):
#             encrypted.append(alphabet[(alphabet.index(char)-alphabet.index(key[i % key_len]))] if char in alphabet else char)
#         return ''.join(encrypted)


class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.alphabet = list(alphabet)
        self.key = [alphabet.index(i) for i in key]

    def encode(self, text):
        return "".join([self.alphabet[(self.alphabet.index(text[i]) + self.key[i % len(self.key)]) % len(self.alphabet)]
                        if text[i] in self.alphabet else text[i] for i in range(len(text))])

    def decode(self, text):
        return "".join([self.alphabet[(self.alphabet.index(text[i]) - self.key[i % len(self.key)]) % len(self.alphabet)]
                        if text[i] in self.alphabet else text[i] for i in range(len(text))])
