# https://www.codewars.com/kata/565b112d09c1adfdd500019c/train/python

# def nth_char(words):
# 	return "".join([words[i][i] for i in range(len(words))])


def nth_char(words):
	return ''.join(w[i] for i,w in enumerate(words))
