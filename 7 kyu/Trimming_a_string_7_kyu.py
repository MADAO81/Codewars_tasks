# https://www.codewars.com/kata/563fb342f47611dae800003c/train/python


# def trim(phrase, size):
#     return phrase if size >= len(phrase) else phrase[:size if len(phrase) < 4 or size < 4 else (size-3)]+ "..."


def trim(phrase, size):
    if len(phrase) <= size:
        return phrase
    elif size <= 3:
        return phrase[:size] + "..."
    else:
        return phrase[:size-3] + "..."
