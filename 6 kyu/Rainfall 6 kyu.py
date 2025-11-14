# https://www.codewars.com/kata/56a32dd6e4f4748cc3000006/train/python

import re

def mean(town, strng):
    try:
        i = re.split("[:, \n]", strng).index(town)
        s = []
        for e in range(i+2, i+25, 2):
            s.append(float(re.split("[:, \n]", strng)[e]))
        return sum(s)/12
    except:
        return -1


def variance(town, strng):
    try:
        if re.search(town, strng) == None:
            return -1
        i = re.split("[:, \n]", strng).index(town)
        s = []
        for e in range(i+2, i+25, 2):
            s.append(float(re.split("[:, \n]", strng)[e]))
        var = [(sum(s)/12) - x for x in s]
        doubled = []
        for e in var:
            doubled.append(e**2) 
        return sum(doubled)/12
    except:
        return -1
