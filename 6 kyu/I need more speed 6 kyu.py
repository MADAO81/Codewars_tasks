# I need more speed!
# Write a function that will take in any array and reverse it.

# Sounds simple doesn't it?

# NOTES:

# Array should be reversed in place! (no need to return it)
# Usual builtins have been deactivated. Don't count on them.
# You'll have to do it fast enough, so think about performances

def reverse(seq):
    new_seq = list()
    for i in range(len(seq)):
        new_seq.append(seq.pop())
    seq.extend(new_seq)


# def reverse(seq): 
#     for i in range(len(seq)//2): 
#         seq[i], seq[len(seq)-1-i] = seq[len(seq)-1-i], seq[i]
