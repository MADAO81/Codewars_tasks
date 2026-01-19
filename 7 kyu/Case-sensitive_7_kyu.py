# Case-sensitive!
# Your task is very simple. Given an input string s, case_sensitive(s), 
# check whether all letters are lowercase or not. Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.

# For example, case_sensitive('codewars') returns [True, []], but case_sensitive('codeWaRs') returns [False, ['W', 'R']].

# def case_sensitive(s):
#     result = []
#     for ch in list(s):
#         if ch == ch.upper():
#             result.append(ch)
#     if result == []:
#         return [True, result]
#     else:
#         return [False, result]


def case_sensitive(s):
    return [s.islower() or not s, [c for c in s if c.isupper()]]
