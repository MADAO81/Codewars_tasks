# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python



# import re
# from collections import Counter

# top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]

from collections import Counter
import re

def top_3_words(text):
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in c.most_common(3)]


