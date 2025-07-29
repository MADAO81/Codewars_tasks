# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26/solutions/python


# def multiply(m1,m2):
#     x = m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0]
#     y = m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]
#     z = m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0]
#     w = m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]
#     return [[x,y],[z,w]]

# def fib(n):
#     r = [[1,0],[0,1]]
#     t = [[0,1],[1,1]]
#     if n < 0:
#         n,t = -n, [[-1,1],[1,0]]
#     while n>0:
#         if n&1 > 0:
#             r = multiply(t,r)
#         t = multiply(t,t)
#         n >>=1
#     return r[0][1]


def fib(n):
  if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
  a = b = x = 1
  c = y = 0
  while n:
    if n % 2 == 0:
      (a, b, c) = (a * a + b * b,
                   a * b + b * c,
                   b * b + c * c)
      n /= 2
    else:
      (x, y) = (a * x + b * y,
                b * x + c * y)
      n -= 1
  return y
