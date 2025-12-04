# https://www.codewars.com/kata/5697fb83f41965761f000052/train/python

# def filter_long_words(sentence, n):
#     result = []
#     for word in sentence.split():
#         if len(word)>n:
#             result.append(word)
#     return result

def filter_long_words(sentence,long):
    return [word for word in sentence.split() if len(word) > long]
