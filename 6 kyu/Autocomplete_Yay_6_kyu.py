#https://www.codewars.com/kata/5389864ec72ce03383000484/train/python


# def autocomplete(input_, dictionary):
#     input_filtered = ""
#     for character in input_:
#         if character >= 'a' and character <= 'z':
#             input_filtered += character
            
#     result = []
#     for word in dictionary:
#         if word.lower().startswith(input_filtered):
#             result.append(word)
#         if len(result) >= 5:
#             break;
    
#     return result



def autocomplete(input_, dictionary):
    input = ''.join(list(filter(lambda x:x.isalpha(), input_.lower())))
    return list(filter(lambda x: x.lower().startswith(input), dictionary))[:5]
