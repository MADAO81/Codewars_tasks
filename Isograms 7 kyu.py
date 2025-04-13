# Isograms
# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    string = string.lower()
    return len(set(string)) == len(string)


# def is_isogram(string):
#     return len(string) == len(set(string.lower()))

# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1: return False
#     return True

# В типе set не может быть дубликатов, поэтому, когда строка преобразуется в один элемент,
# она разбивается на символы.
# Разница в длине показывает, сколько повторяющихся символов было (но НЕ сами символы)