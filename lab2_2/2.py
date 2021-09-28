import turtle

turtle.shape('turtle')
def one():
    turtle.right(90)
    turtle.forward(50)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(70)
    turtle.right(135)
    turtle.forward(100)
    turtle.right(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)

def four():
    turtle.right(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.forward(50)

def seven():
    turtle.pendown()
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(70)
    turtle.left(45)
    turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)


def zero():
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)

turtle.penup()

a=(one(),four(),one(),seven(),zero(),zero())

for item in a:
    item
