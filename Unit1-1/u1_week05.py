import turtle as t
# Task: Create a face using turtle
# Draw head
# Draw eyes

# Draw Rosy, red cheeks

t.speed(0)
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

# Function calls below here
myCircle(100, "green")
myMove(-50, 100) # move to create LEFT eye
myCircle(20, "black")
myMove(-50, 115)
myCircle(5, "white")
myMove(50, 100) # move to create RIGHT eye
myCircle(20, "black")
myMove(50, 115)
myCircle(5, "white")
# Draw nose
myMove(0, 75)
myCircle(30, "red")
myMove(-5, 85)
myCircle(2, "black")
myMove(5, 85)
myCircle(2, "black")
# Draw Rosy, red cheeks
myMove(-60, 50)
myCircle(20, "pink")
myMove(60, 50)
myCircle(20, "pink")
# Draw mouth
myMove(-20, 50)
t.seth(-90)
t.circle(20, 180)
# always use the following as the last line of code in Python
t.hideturtle() # hide turtle
t.Screen().exitonclick()
