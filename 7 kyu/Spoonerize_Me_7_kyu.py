# https://www.codewars.com/kata/56b8903933dbe5831e000c76/train/python

def spoonerize(words):
    words = words.split()
    return f"{words[1][:1]+words[0][1:]} {words[0][:1]+words[1][1:]}"
