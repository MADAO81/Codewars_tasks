# Bit Counting
# Write a function that takes an integer as input, and returns the number 
# of bits that are equal to one in the binary representation of that number. 
# You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    count = []
    for ch in bin(n):
        if ch == "1":
            count.append(ch)
    result = [int(item) for item in count]
    return sum(result)
    
# def countBits(n):
#     return bin(n).count("1")
