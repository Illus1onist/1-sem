import turtle
import random as r


N=10

velox=[0]*N
veloy = [0] * N
coordx = [0] * N
coordy = [0] * N

for i in range (N):
    coordx[i]=r.randint(-100,100)
    coordy[i] = r.randint(-100, 100)


pool = [turtle.Turtle(shape='turtle') for i in range (N)]
for unit in pool:
    unit.penup()
    unit.goto(coordx[i],coordy[i])


for t in range (100):
    for i in range(N):
        ax=0
        ay=0
        for z in range(N):
            if coordx[z]!=coordx[i]:
                ax=ax-5/(coordx[z]-coordx[i])/abs(coordx[z]-coordx[i])
        for z in range(N):
            if coordy[z]!=coordy[i]:
                ay=ay-5/(coordy[z]-coordy[i])/abs(coordy[z]-coordy[i])

        velox[i]=velox[i]+ax
        veloy[i]=veloy[i]+ay
        coordx[i]=coordx[i]+velox[i]
        coordy[i]=coordy[i]+veloy[i]

        pool[i].goto(coordx[i],coordy[i])