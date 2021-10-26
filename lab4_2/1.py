import pygame
from pygame.draw import *
from random import randint


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
#N=40            #максимальное количество шариков



#функция для рисования нового шарика с случайными
class Ball():
    def __init__(self):
        self.x=0
        self.y = 0
        self.r = 0
        self.vx = 0
        self.vy = 0
        self.color = RED


    def move(self):
        self.x=int(self.x+self.vx*0.1)
        self.y = int(self.y + self.vy*0.1)
        if (self.x<self.r):
            self.x = self.x + 2
            self.vx=-self.vx
        if (self.x>1200-self.r):
            self.x=self.x-2
            self.vx = -self.vx
        if (self.y<self.r):
            self.y = self.y + 2
            self.vy=-self.vy
        if (self.y>900-self.r):
            self.y = self.y - 2
            self.vy = -self.vy
        circle(screen, self.color, (self.x, self.y), self.r)

global ball

ball = []

def new_ball():
    global k, ball
    ball.append(Ball())
    ball[k].x = randint(100, 1100)
    ball[k].y = randint(100, 800)
    ball[k].r = randint(50, 100)

    diapasonx = list(range(-25, -10)) + list(range(10, 25))  # диапазон скоростей
    diapasony = list(range(-25, -10)) + list(range(10, 25))

    ball[k].vx = diapasonx[randint(0, len(diapasonx) - 1)]
    ball[k].vy = diapasony[randint(0, len(diapasony) - 1)]

    ball[k].color=COLORS[randint(0, 5)]

    pygame.draw.circle(screen, ball[k].color, (ball[k].x, ball[k].y), ball[k].r)

    k = k + 1


pygame.display.update()
clock = pygame.time.Clock()
finished = False

def Text(score):
    f = pygame.font.Font(None, 36)
    text = f.render('Score:' + str(score), 1, (180, 0, 0))
    screen.blit(text, (250, 20))

while not finished:
    clock.tick(FPS)
    #часы
    a = a + 1

    #реализация движения шаров
    for i in range(k):
        ball[i].move()
    #добавление на экран счета
    Text(score)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (k):

                if (event.pos[0] - ball[i].x) ** 2 + (event.pos[1] - ball[i].y) ** 2 <= ball[i].r ** 2:       #реализация уничтожение при клике
                    screen.fill(BLACK)

                    score=score+1           #увеличение счета
                    k = k - 1               #уменьшение количества шариков

                    Text(score)
                    pygame.display.update()
                    #сдвиг всего массива
                    for j in range(i,k):
                        ball[j].x = ball[j+1].x
                        ball[j].y = ball[j+1].y
                        ball[j].r = ball[j+1].r
                        ball[j].vx = ball[j+1].vx
                        ball[j].vy = ball[j+1].vy
                        ball[j].color=ball[j+1].color
                    ball.pop(k)
                    #отображение нового набора шаров
                    for s in range(k):
                        pygame.draw.circle(screen, ball[s].color, (ball[s].x, ball[s].y), ball[s].r)
                    pygame.display.update()
                    break
    #подготовка к новому начала цикла
    screen.fill(BLACK)
    #добавление на экран и в массив с информацией нового шара

    if a==FPS:
        a=0
        new_ball()



pygame.quit()