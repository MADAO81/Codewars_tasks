# https://www.codewars.com/kata/57fb142297e0860073000064/train/python

# def product(st):
#     count_exl = st.count("!")
#     count_question = st.count("?")
#     return count_exl * count_question

def product(s):
    return s.count("?")*s.count("!")
