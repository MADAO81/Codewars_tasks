# https://www.codewars.com/kata/57a93f93bb9944516d0000c1/train/python

# class Dictionary(dict):
#     newentry = dict.__setitem__
    
#     def look(self, key):
#         return self.get(key, f"Can't find entry for {key}")


class Dictionary(object):
    def __init__(self):
        self.my_dict = {}

    def look(self, key):
        return self.my_dict.get(key, "Can't find entry for {}".format(key))

    def newentry(self, key, value):
        """ new_entry == PEP8 (forced by Codewars) """
        self.my_dict[key] = value
