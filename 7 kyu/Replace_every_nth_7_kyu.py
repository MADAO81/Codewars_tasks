# https://www.codewars.com/kata/57fcaed83206fb15fd00027a/train/python

# def replace_nth(text, n, old_value, new_value):
#     if n <= 0: return text
#     s = list(text)
#     l = [i for i, c in enumerate(s) if c == old_value]
#     for i in l[n-1::n]: s[i] = new_value
#     return ''.join(s)


def replace_nth(text, n, old, new):
    count = 0
    res = ""
    for c in text:
        if c==old: 
            count+=1
            if count ==n:
                res+=new
                count=0
                continue
        res+=c
    return res
