# Write a program that outputs the top n elements from a list.

# Example:

# k = 2; list = [7, 6, 5, 4, 3, 2, 1]
# ==> [6, 7]


# def largest(n,xs):
#   return (sorted(xs, reverse=True)[0:n])[::-1]

def largest(n, xs):
    if n == 0:
        return []
    return sorted(xs)[-n:]
