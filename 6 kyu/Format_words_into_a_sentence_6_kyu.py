# https://www.codewars.com/kata/51689e27fe9a00b126000004/train/python

# def format_words(words):
#     return ', '.join(word for word in words if word)[::-1].replace(',', 'dna ', 1)[::-1] if words else ''
  

def format_words(words):
    if not words:
        return ''
    words = [word for word in words if word]
    if len(words) > 1:
        return  ', '.join(words[:-1]) + ' and ' + words[-1]
    else:
        return words[0] if len(words) else ''
