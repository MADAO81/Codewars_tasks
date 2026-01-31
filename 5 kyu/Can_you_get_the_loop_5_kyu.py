# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python

def loop_size(node):
    turtle, rabbit = node.next, node.next.next

    while turtle != rabbit:
        turtle = turtle.next
        rabbit = rabbit.next.next
  
    count = 1
    rabbit = rabbit.next
    while turtle != rabbit:
        count += 1
        rabbit = rabbit.next

    return count
