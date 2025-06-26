# Decode the Morse code
# In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and digital data communication channels, it still has its use in some applications around the world.
# The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

# NOTE: Extra spaces before or after the code have no meaning and should be ignored.

# In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special codes are treated as single special characters, and usually are transmitted as separate words.

# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

# For example:

# decode_morse('.... . -.--   .--- ..- -.. .')
# #should return "HEY JUDE"


from preloaded import MORSE_CODE

def decode_morse(morse_code):
    return ' '.join(''.join(MORSE_CODE[i] for i in word.split(' ')) for word in morse_code.strip().split("   "))


# def decodeMorse(morse_sequence):
#     words = []
#     for morse_word in morse_sequence.split('   '):
#         word = ''.join(MORSE_CODE.get(morse_char, '') for morse_char in morse_word.split(' '))
#         if word:
#             words.append(word)
#     return ' '.join(words)
