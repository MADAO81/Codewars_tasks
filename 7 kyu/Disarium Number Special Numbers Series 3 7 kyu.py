# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/python

# def disarium_number(number):
#     if sum([int(el)**(i+1) for i,el in enumerate(str(number))])==number:
#         return "Disarium !!"
#     else:
#         return "Not !!"


# def disarium_number(number):
#     a=0
#     for j,i in enumerate(str(number)):
#         a+=int(i)**(j+1)
#     return 'Disarium !!' if a==number else 'Not !!'


def disarium_number(n):
    return "Disarium !!" if n == sum(int(d)**i for i, d in enumerate(str(n), 1)) else "Not !!"
