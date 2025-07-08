# https://www.codewars.com/kata/54b72c16cd7f5154e9000457/train/python

# from itertools import groupby

# def decode_bits(bits):
#     bits, morse_code = bits.strip('0'), ''
#     pattern = {'111': '-', '1': '.', '0' * 7: ' ', '000': '#', '0': ''}
#     time_unit = min(len(list(group)) for _, group in groupby(bits))
#     pattern = {k * time_unit: v for k, v in pattern.items()}
#     while bits:
#         for code, symbol in pattern.items():
#             while bits.startswith(code):
#                 morse_code += symbol
#                 bits = bits[len(code):]
#     return morse_code

# def decode_morse(morseCode):
#     morseCode = [seq.split('#') for seq in morseCode.split()]
#     return ' '.join(''.join(MORSE_CODE[symbol] for symbol in word) for word in morseCode)


def decodeBits(bits):
    import re
    
    # remove trailing and leading 0's
    bits = bits.strip('0')
    
    # find the least amount of occurrences of either a 0 or 1, and that is the time hop
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
    
    # hop through the bits and translate to morse
    return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[l] for l in w.split()) for w in morseCode.split('   '))
