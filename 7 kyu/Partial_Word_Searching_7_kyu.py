# https://www.codewars.com/kata/54b81566cd7f51408300022d/train/python


# def word_search(query, seq):
#     query = query.lower()
#     result = [x for x in seq if query in x.lower()]
#     return result if result else ['None']



def word_search(query, seq):
    return [x for x in seq if query.upper() in x.upper()] or ["None"]
