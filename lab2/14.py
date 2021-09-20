import turtle

turtle.shape('turtle')
turtle.left (180)
def star(n):
    for i in range (1,n+1):
        turtle.forward(100)
        turtle.left (180-360/2/n)



star(5)

star(11)