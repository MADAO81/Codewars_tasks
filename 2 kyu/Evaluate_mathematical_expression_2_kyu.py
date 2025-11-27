# https://www.codewars.com/kata/52a78825cdfc2cfc87000005/train/python


# solution_#_1

# import operator

# OP_DICT = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv
# }

# def tokenize(expression):
#     tokens = []
#     st = []
#     op = dict()
#     cl = dict()
    
#     i = 0
#     while i < len(expression):
#         if expression[i] == " ":
#             i += 1
#             continue
#         if expression[i].isdigit():
#             j = i
#             while i + 1 < len(expression) and (expression[i+1].isdigit() or expression[i+1]=="."):
#                 i +=1
#             tokens.append(float(expression[j:i+1]))
#         else:
#             if expression[i] == "(":
#                 st.append(len(tokens))
#             if expression[i] == ")":
#                 j = len(tokens)
#                 op[j] = st.pop()
#                 cl[op[j]] = j
#             tokens.append(expression[i])
            
#         i += 1
#     return tokens, op, cl
        
# def calc(e):
#     tokens, op, cl = tokenize(e)

#     def eval_muldiv(tokens):
#         v, o = 1, '*'
#         for token in tokens:
#             if isinstance(token, float):
#                 v = OP_DICT[o](v, token)
#             else:
#                 o = token
#         return v
    
#     def dfs(idx_st, idx_en):
#         idx = idx_st
#         tokens_no_par = []
#         while idx <= idx_en:
#             if tokens[idx] == '(':
#                 v = dfs(idx + 1, cl[idx] - 1)
#                 tokens_no_par.append(v)
#                 idx = cl[idx]
#             else:
#                 tokens_no_par.append(tokens[idx])

#             idx += 1
#         tokens_no_neg = []
#         idx = 0
#         while idx < len(tokens_no_par):
#             if tokens_no_par[idx] != '-':
#                 tokens_no_neg.append(tokens_no_par[idx])
#             else:
#                 if idx > 0 and isinstance(tokens_no_par[idx - 1], float):
#                     tokens_no_neg.append('-')
#                 else:
#                     j = idx
#                     while not isinstance(tokens_no_par[idx], float):
#                         idx += 1
#                     n_neg = idx - j
#                     v = tokens_no_par[idx] * ((-1) ** (n_neg % 2))
#                     tokens_no_neg.append(v)
#             idx += 1
#         idx_addsub = [-1]
#         for idx, token in enumerate(tokens_no_neg):
#             if token == '+' or token == '-':
#                 idx_addsub.append(idx)

#         v, o = 0, '+'
#         for i in range(1, len(idx_addsub)):
#             j, k = idx_addsub[i - 1], idx_addsub[i]
#             v1 = eval_muldiv(tokens_no_neg[j + 1 : k])
#             v = OP_DICT[o](v, v1)
#             o = tokens_no_neg[k]

#         v = OP_DICT[o](v, eval_muldiv(tokens_no_neg[idx_addsub[-1] + 1:]))
#         return v
            
#     return dfs(0, len(tokens) - 1)



# solution_#_2

import re
from operator import mul, truediv as div, add, sub


OPS = {'*': mul, '/': div, '-': sub, '+': add}


def calc(expression):
    tokens  = re.findall(r'[.\d]+|[()+*/-]', expression)
    return parse_AddSub(tokens, 0)[0]


def parse_AddSub(tokens, iTok):
    
    v, iTok = parse_MulDiv(tokens, iTok)
    
    while iTok < len(tokens) and tokens[iTok] != ')':
        tok   = tokens[iTok]
        if tok in '-+': 
            v2, iTok = parse_MulDiv(tokens, iTok+1)
            v = OPS[tok](v, v2)
    
    return v, iTok
    

def parse_MulDiv(tokens, iTok):
    
    v, iTok = parse_Term(tokens, iTok)
    
    while iTok < len(tokens) and tokens[iTok] in '*/': 
        op = tokens[iTok]
        v2, iTok = parse_Term(tokens, iTok+1)
        v = OPS[op](v, v2)
    
    return v, iTok


def parse_Term(tokens, iTok):
    tok = tokens[iTok]
    
    if tok == '(':
        v, iTok = parse_AddSub(tokens, iTok+1)
        if iTok < len(tokens) and tokens[iTok] != ')': raise Exception()
        
    elif tok == '-':
        v, iTok = parse_Term(tokens, iTok+1)
        v, iTok = -v, iTok-1
        
    else:
        v = float(tok)
    
    return v, iTok+1
