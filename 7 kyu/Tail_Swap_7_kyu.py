# https://www.codewars.com/kata/5868812b15f0057e05000001/train/python

# def tail_swap(strings):
#     part_one = strings[0].split(':')
#     part_two = strings[1].split(':')
#     part_one[1],part_two[1] = part_two[1], part_one[1]
#     return [':'.join(part_one),':'.join(part_two)]


def tail_swap(strings):
    head0, tail0 = strings[0].split(':')
    head1, tail1 = strings[1].split(':')
    return [head0 + ':' + tail1, head1 + ':' + tail0]
