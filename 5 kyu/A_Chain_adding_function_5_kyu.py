# https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

# class Addition(int):
#     def __call__(self, value):
#         return Addition(self+value)
# def add(n):
#     return Addition(n)

class add(int):
    def __call__(self,n):
        return add(self+n)
