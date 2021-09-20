import turtle

turtle.shape('turtle')

turtle.right(90)
for i in range (1, 10):
    turtle.penup()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.pendown()
    turtle.forward(50 * 2 * i)
    turtle.left(90)
    turtle.forward(50 * 2 * i)
    turtle.left(90)
    turtle.forward(50 * 2 * i)
    turtle.left(90)
    turtle.forward(50 * 2 * i)