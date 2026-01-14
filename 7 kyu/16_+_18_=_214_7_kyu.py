# https://www.codewars.com/kata/5effa412233ac3002a9e471d/train/python

# def add(num1, num2):
#     num1 = str(num1)
#     num2 = str(num2)
#     pad = len(num1) if len(num1) > len(num2) else len(num2)
#     num1, num2 = num1.zfill(pad), num2.zfill(pad)
#     num1, num2 = num1[::-1], num2[::-1]
#     return int(''.join([str(int(i)+int(j)) for i,j in zip(num1,num2)][::-1]))



# def add(*args):
#     a, b = map(str, sorted(args))
#     a = a.zfill(len(b))
#     result = [int(x) + int(y) for x, y in zip(a, b)]
#     return int("".join(map(str, result)))


def add(a,b):
    s = ""
    while a+b:
        a,p = divmod(a,10)
        b,q = divmod(b,10)
        s = str(p+q)+s
    return int(s or'0')
