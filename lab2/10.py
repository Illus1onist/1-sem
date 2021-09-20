import turtle

turtle.shape('turtle')
def bystrelka():
    for i in range (1,180):
        turtle.forward(2)
        turtle.right(2)

def notbystrelka():
    for i in range (1,180):
        turtle.forward(2)
        turtle.left(2)

notbystrelka()
bystrelka()
turtle.left(60)
notbystrelka()
bystrelka()
turtle.left(60)
notbystrelka()
bystrelka()