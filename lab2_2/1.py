import turtle
import random as r

turtle.shape('turtle')

for i in range (1000) :
    turtle.forward(50*r.random())
    turtle.left(r.random()*360)