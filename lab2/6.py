import turtle

turtle.shape('turtle')

n=12
for i in  range (1,n):
    turtle.right(360/n)
    turtle.forward(50)
    turtle.stamp()
    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(180)
    turtle.pendown()