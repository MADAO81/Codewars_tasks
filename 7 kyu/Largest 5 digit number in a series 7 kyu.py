# In the following 6 digit number:
# 283910
# 91 is the greatest sequence of 2 consecutive digits.
# In the following 10 digit number:
# 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.
# Complete the solution so that it returns the greatest sequence of five consecutive digits found within the number given.
# The number will be passed in as a string of only digits. 
# It should return a five digit integer. The number passed may be as large as 1000 digits.
# Adapted from ProjectEuler.net

def solution(digits):
    numlist = [int(digits[i:i+5]) for i in range(0,len(digits)-4)]
    return max(numlist)

# def solution(digits):
#     maximum = max(digits)
#     result = []
#     for e, d in enumerate(digits[:-4]):
#         if d == maximum:
#             result.append(int(digits[e:e+5]))
#     return max(result)
