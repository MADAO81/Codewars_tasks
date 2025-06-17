# Cats in hats
# The Cat In The Hat has cat A under his hat, cat A has cat B under his hat and so on until Z
# The Cat In The Hat is 2,000,000 cat units tall.
# Each cat is 2.5 times bigger than the cat underneath their hat.
# Find the total height of the cats if they are standing on top of one another.
# Counting starts from the Cat In The Hat
# n = the number of cats
# fix to 3 decimal places.

def height(n):
    height_cat = 2000000
    count = 0
    cats = []
    result = 0
    while count <= n:
        cats.append(height_cat)
        height_cat = height_cat / 2.5
        count +=1
    result = sum(cats)
    return (f"{result:.3f}")
    

# def height(n):
#     result = (2000000 * (1 - 0.4 ** (n + 1))) / (1 - 0.4)
#     return '{:.3f}'.format(result)

# def height(n):
#     height = cat = 2000000
#     for i in range(n):
#         cat /= 2.5
#         height += cat
#     return f'{height:.3f}'
