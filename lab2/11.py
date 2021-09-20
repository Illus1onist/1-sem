import turtle

turtle.shape('turtle')
def bystrelka(r):
    for i in range (1,180):
        turtle.forward(1*r/50)
        turtle.right(2)

def notbystrelka(r):
    for i in range (1,180):
        turtle.forward(1*r/50)
        turtle.left(2)

a=50
for i in range (1,7):
    bystrelka(a)
    notbystrelka(a)
    a=a+10
