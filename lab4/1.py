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
a=1             #счетчик времени
k=0             #количество шариков на экране
score=0         #счет
N=40            #максимальное количество шариков
b=np.eye(N,5)   #массив для координат, радиуса и скорости кажого шарика
c=np.eye(N,3)   #массив для цвета этих шариков


#функция для рисования нового шарика с случайными
def new_ball():

    global x,y,r,k,vx,vy
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(50, 100)

    diapasonx=list(range(-25,-10))+list(range(10,25))           #диапазон скоростей
    diapasony = list(range(-25, -10)) + list(range(10, 25))

    vx = diapasonx[randint(0,len(diapasonx)-1)]
    vy = diapasony[randint(0,len(diapasony)-1)]

    color = COLORS[randint(0, 5)]

    circle(screen, color, (x, y), r)    #создание шара
    #запись всех параметров в массивы
    b[k][0] = x
    b[k][1] = y
    b[k][2] = r
    b[k][3] = vx
    b[k][4] = vy
    c[k]=color
    #увеличение количества шариков
    k=k+1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

f = pygame.font.Font(None, 36)
text = f.render('Score:' + str(score), 1, (180, 0, 0))
screen.blit(text, (250, 20))

while not finished:
    clock.tick(FPS)
    #часы
    a = a + 1

    #реализация движения шаров
    for i in range(k):
        b[i][0] = b[i][0]+b[i][3]*0.1
        b[i][1] = b[i][1]+b[i][4]*0.1
        if b[i][0]-b[i][2]<=0 or b[i][0]+b[i][2]>=1200:
            b[i][3]=-b[i][3]
        if b[i][1]-b[i][2]<=0 or b[i][1]+b[i][2]>=900:
            b[i][4]=-b[i][4]
        #и их перерисовки
        circle(screen, c[i], (int(b[i][0]), int(b[i][1])), int(b[i][2]))

    #добавление на экран счета
    text = f.render('Score:' + str(score), 1, (180, 0, 0))
    screen.blit(text, (250, 20))
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (k):

                if (event.pos[0] - b[i][0]) ** 2 + (event.pos[1] - b[i][1]) ** 2 <= b[i][2] ** 2:       #реализация уничтожение при клике
                    screen.fill(BLACK)
                    score=score+1           #увеличение счета
                    k = k - 1               #уменьшение количества шариков

                    text = f.render('Score:' + str(score), 1, (180, 0, 0))          #добавление нового счетчика на экран (исправленного)
                    screen.blit(text, (250, 20))

                    #сдвиг всего массива
                    for j in range(i,k):
                        b[j][0] = b[j + 1][0]
                        b[j][1] = b[j + 1][1]
                        b[j][2] = b[j + 1][2]
                        b[j][3] = b[j + 1][3]
                        b[j][4] = b[j + 1][4]
                        c[j] = c[j+1]
                    #отображение нового набора шаров
                    for s in range(k):
                        circle(screen, c[s], (int(b[s][0]), int(b[s][1])), int(b[s][2]))
                    pygame.display.update()
                    break
    #подготовка к новому начала цикла
    screen.fill(BLACK)
    #добавление на экран и в массив с информацией нового шара
    if a==30:
        a=0
        new_ball()


pygame.quit()