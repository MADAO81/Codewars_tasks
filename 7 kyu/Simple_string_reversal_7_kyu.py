# https://www.codewars.com/kata/5a71939d373c2e634200008e/train/python

# def solve(s):
#     s_temp = list(s[::-1].replace(" ",""))
#     return "".join(" " if i == " " else s_temp.pop(0) for i in s)


# def solve(s):
#     space_index=[i for i in range(len(s)) if s[i]==" "]    #find index of saces  
#     s = ''.join(s.split())                                 #remove spaces
#     s=s[::-1]                                              #reverse the string    
#     for i in space_index:                                  #add spaces again to exactly same place before
#         s = s[:i] + " " + s[i:]
#     return s

def solve(s):
    it = reversed(s.replace(' ',''))
    return ''.join(c if c == ' ' else next(it) for c in s)
