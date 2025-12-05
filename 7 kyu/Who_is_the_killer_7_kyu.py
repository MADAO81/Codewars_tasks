# https://www.codewars.com/kata/5f709c8fb0d88300292a7a9d/train/python

# def killer(suspect_info, dead):
#     for suspect,seen_people in suspect_info.items():
#         if all(person in seen_people for person in dead):
#             return suspect
#     return None

def killer(info, dead):
    for name, seen in info.items():
        if set(dead) <= set(seen):
            return name
