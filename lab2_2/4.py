import turtle

vx = 5
vy = 20
g = 2
angle = 45
x = -500
y = 1
for i in range(1000):
    if y<=0:
        vy=-vy*0.7

        y=y+1
    vy=vy-g*0.05
    x=x+vx*0.05
    y=y+vy*0.05
    turtle.goto(x,y)
