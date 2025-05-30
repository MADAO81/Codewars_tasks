# Testing 1-2-3
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

# Write a function which takes a list of strings and returns each line prepended by the correct number.

# The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)

# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
    counter = 1
    number_line = 0
    result = []
    for i in lines:
        number_line = str(counter) + ": " + i
        result.append(number_line)
        counter +=1
    return result


# def number(lines):
# 	return [str(x+1) + ": " + lines[x] for x in range(len(lines))]
