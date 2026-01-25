# https://www.codewars.com/kata/57ae18c6e298a7a6d5000c7a/train/python


# def replace_all(obj, find, replace):
#     result = [el if el != find else replace for el in obj]
#     return ''.join(result) if isinstance(obj, str) else result


# def replace_all(obj, find, replace):
#     if type(obj) == list:
#         return [replace if i == find else i for i in obj]
#     else:
#         return obj.replace(find, replace)


def replace_all(obj, find, replace):
  if isinstance(obj, str):
    return obj.replace(find, replace)
  elif isinstance(obj, list):
    return [x if x != find else replace for x in obj]
