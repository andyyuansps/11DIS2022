import turtle as t

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [0, 1]
    fibs = [0, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


t.speed(0)
x = fib(15)
xaxis = (-350)
print(x)
for i in x:
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(i)
    t.end_fill()
    t.write(i)
    myMove(xaxis,-10)
    xaxis += i*4.1

t.hideturtle() # hide turtle
t.Screen().exitonclick()
