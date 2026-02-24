# https://www.codewars.com/kata/5583d268479559400d000064/train/python


# import textwrap

# def binary_to_string(binary):
#     text = textwrap.wrap(binary,8)
#     text = ' '.join(text)
#     return ''.join([chr(int(b,2)) for b in text.split()])



# def binary_to_string(binary):
#     return "".join(chr(int(binary[i:i+8],2)) for i in range(0,len(binary),8))



def binary_to_string(binary):
    return "".join( [ chr( int(binary[i: i+8], 2) ) for i in range(0, len(binary), 8) ] )
