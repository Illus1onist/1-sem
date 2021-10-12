import pygame
from pygame.draw import *
from random import randint
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global a,k
a=1
k=0
score=0
N=40
b=np.eye(N,5)
c=np.eye(N,3)
def new_ball():
    '''рисует новый шарик '''
    global x,y,r,k,vx,vy
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(50, 100)

    diapasonx=list(range(-25,-10))+list(range(10,25))
    diapasony = list(range(-25, -10)) + list(range(10, 25))
    vx = diapasonx[randint(0,len(diapasonx)-1)]
    vy = diapasony[randint(0,len(diapasony)-1)]
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    b[k][0] = x
    b[k][1] = y
    b[k][2] = r
    b[k][3] = vx
    b[k][4] = vy
    c[k]=color

    k=k+1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

f = pygame.font.Font(None, 36)
text = f.render('Score:' + str(score), 1, (180, 0, 0))
screen.blit(text, (250, 20))

while not finished:
    clock.tick(FPS)

    a = a + 1
    for i in range(k):
        b[i][0] = b[i][0]+b[i][3]*0.1
        b[i][1] = b[i][1]+b[i][4]*0.1
        if b[i][0]-b[i][2]<=0 or b[i][0]+b[i][2]>=1200:
            b[i][3]=-b[i][3]
        if b[i][1]-b[i][2]<=0 or b[i][1]+b[i][2]>=900:
            b[i][4]=-b[i][4]



        circle(screen, c[i], (int(b[i][0]), int(b[i][1])), int(b[i][2]))
    text = f.render('Score:' + str(score), 1, (180, 0, 0))
    screen.blit(text, (250, 20))
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (k):
                if (event.pos[0] - b[i][0]) ** 2 + (event.pos[1] - b[i][1]) ** 2 <= b[i][2] ** 2:
                    screen.fill(BLACK)
                    score=score+1
                    k = k - 1

                    text = f.render('Score:' + str(score), 1, (180, 0, 0))
                    screen.blit(text, (250, 20))

                    for j in range(i,k):
                        b[j][0] = b[j + 1][0]
                        b[j][1] = b[j + 1][1]
                        b[j][2] = b[j + 1][2]
                        b[j][3] = b[j + 1][3]
                        b[j][4] = b[j + 1][4]
                        c[j] = c[j+1]
                    for s in range(k):
                        circle(screen, c[s], (int(b[s][0]), int(b[s][1])), int(b[s][2]))
                    pygame.display.update()
                    break

    screen.fill(BLACK)
    if a==30:
        a=0
        new_ball()


pygame.quit()