# https://www.codewars.com/kata/57d1f36705c186d018000813/train/python

# import re
# def gordon(a):
#     a = re.sub(r'(\w+)\b', r'\1' + '!!!!',a )
#     a = re.sub(r'[a]', '@', a)
#     a =  re.sub(r'[eiuo]', '*',a)
#     return a.upper()


def gordon(a):
	return '!!!! '.join(a.upper().split()).translate(str.maketrans('AEIOU', '@****'))+'!!!!'
