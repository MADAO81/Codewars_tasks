# Find the capitals
# Write a function that takes a single non-empty string of only lowercase and 
# uppercase ascii letters (word) as its argument, and returns an ordered list 
# containing the indices of all capital (uppercase) letters in the string.

# Example (Input --> Output)
# "CodEWaRs" --> [0,3,4,6]

def capitals(word):
    somelist = []
    count = 0
    for ch in word:
        if ch.isupper():
            somelist.append(count)
        count += 1
    return somelist
