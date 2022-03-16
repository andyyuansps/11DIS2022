def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

import turtle as t


def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

# Eye function
def myCircle(size, col):
    t.fillcolor(col)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


num1 = fib(1)

for i in range(10):
  t.circle(1)
  myMove(fib(2),fib(2))

