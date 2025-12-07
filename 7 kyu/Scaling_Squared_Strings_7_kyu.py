# https://www.codewars.com/kata/56ed20a2c4e5d69155000301/train/python

# def scale(strng, k, v):
#     output = ''
#     substrings = strng.split('\n')
#     for sub in substrings:
#         temp = ''
#         for char in sub:
#             temp += char * k
#             print(temp)
#         output += (temp +'\n') * v
#         temp = ''
#     return output.strip('\n')


def horizontal(s,k):
	return ''.join(c*k for c in s)

def vertical(s,n):
	return '\n'.join([s]*n)

def scale(s, k, n):
    return '\n'.join([vertical(v,n) for v in [horizontal(h,k) for h in s.split('\n')]]) if s else ''
