# https://www.codewars.com/kata/5898b4b71d298e51b600014b/train/python

# def sort_the_inner_content(words):
#     return ' '.join(i[0]+''.join(sorted(i[1:-1], reverse=True))+i[-1] if len(i)>3 else i for i in words.split())


def sort_the_inner_content(str):
    words = str.split()
    output = []
    
    for word in words:
        if len(word) > 2:
            output.append(word[0] + ''.join(sorted(word[1:-1], reverse=True)) + word[-1])            
        else: output.append(word)
        
    return ' '.join(output)
