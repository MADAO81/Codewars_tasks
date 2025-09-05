# Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

# Your task is to process a string with "#" symbols.

# Examples
# "abc#d##c"      ==>  "ac"
# "abc##d######"  ==>  ""
# "#######"       ==>  ""
# ""              ==>  ""


# def clean_string(s):
#     stk = []
#     for c in s:
#         if c=='#' and stk: stk.pop()
#         elif c!='#':       stk.append(c)
#     return ''.join(stk)


def clean_string(s):
    result = ""
    for ch in s:
        if ch == "#":
            result = result[:-1]
        else:
            result += ch
    return result
