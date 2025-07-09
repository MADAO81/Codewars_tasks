# Your job is to fix the parentheses so that all opening and closing parentheses (brackets) have matching counterparts. 
# You will do this by appending parenthesis to the beginning or end of the string. The result should be of minimum length. Don't add unnecessary parenthesis.

# The input will be a string of varying length, only containing '(' and/or ')'.

# For example:

# Input: ")("
# Output: "()()"

# Input: "))))(()("
# Output: "(((())))(()())"


def fix_parentheses(strng):
    original = strng
    open = "("
    close = ")"
    while "()" in strng:
        strng = strng.replace("()", "")
    opening = open * strng.count(close)
    closing = close * strng.count(open)
    return f"{opening}{original}{closing}"
