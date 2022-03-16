import turtle as t

t.speed(0)

floorWidth = 345
floorLength = 150
numberOfTilesX = 0
numberOfTilesY = 0
squareSize = 0

num1 = floorWidth
num2 = floorLength

if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

squareSize = gcd

t.penup()
t.goto(-200, 0)
t.pendown()

length = 345
width = 150


def rec(x, y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)


rec(length, width)

numberOfTilesX = length / gcd
numberOfTilesY = width / gcd

tilesX = 0
tilesY = 0

while tilesY < numberOfTilesY:
    t.penup()
    t.goto(-200, tilesY * 15)
    while tilesX < numberOfTilesX:
        t.penup()
        t.goto(-200 + tilesX * 15, tilesY * 15)
        t.pendown()
        rec(squareSize, squareSize)
        tilesX += 1
    t.pendown()
    rec(squareSize, squareSize)
    tilesY += 1
    tilesX = 0

t.hideturtle()  # hide turtle
t.Screen().exitonclick()
