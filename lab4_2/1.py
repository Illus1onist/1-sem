import pygame
import pygame
import random


pygame.init()

FPS = 30
screen = pygame.display.set_mode((1100, 800))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

global a,k,s
a=1             #счетчик времени
k=0
s=0         #количество шариков на экране
score=0         #счет
#N=40            #максимальное количество шариков



#функция для рисования нового шарика с случайными
class Star:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 40
        self.vx = 0
        self.vy = 0
        self.color = random.choice(COLORS)


    def move(self):
        g=2.0
        self.vy = self.vy - g
        self.x += self.vx
        self.y -= self.vy
        if self.x>=1100-self.r:
            self.x=1100-self.r
            self.vx=-self.vx
        if self.x<=self.r:
            self.x=self.r
            self.vx=-self.vx
        if self.y>=800-self.r:
            self.vy=-self.vy
            self.y=800-self.r
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

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
        if (self.x>1100-self.r):
            self.x=self.x-2
            self.vx = -self.vx
        if (self.y<self.r):
            self.y = self.y + 2
            self.vy=-self.vy
        if (self.y>800-self.r):
            self.y = self.y - 2
            self.vy = -self.vy
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

global ball

ball = []
star=[]
def new_ball():
    global k,s, ball,star
    if random.uniform(0,1)<0.5:
        ball.append(Ball())
        ball[k].x = random.randint(100, 1000)
        ball[k].y = random.randint(100, 700)
        ball[k].r = random.randint(50, 100)

        diapasonx = list(range(-25, -10)) + list(range(10, 25))  # диапазон скоростей
        diapasony = list(range(-25, -10)) + list(range(10, 25))

        ball[k].vx = diapasonx[random.randint(0, len(diapasonx) - 1)]
        ball[k].vy = diapasony[random.randint(0, len(diapasony) - 1)]

        ball[k].color = COLORS[random.randint(0, 5)]

        pygame.draw.circle(screen, ball[k].color, (ball[k].x, ball[k].y), ball[k].r)

        k = k + 1
    else:
        star.append(Star())
        star[s].x = random.randint(100, 1000)
        star[s].y = random.randint(100, 700)
        star[s].r = random.randint(50, 100)

        diapasonx = list(range(-25, -10)) + list(range(10, 25))  # диапазон скоростей
        diapasony = list(range(-25, -10)) + list(range(10, 25))

        star[s].vx = diapasonx[random.randint(0, len(diapasonx) - 1)]
        star[s].vy = diapasony[random.randint(0, len(diapasony) - 1)]

        star[s].color=COLORS[random.randint(0, 5)]

        pygame.draw.circle(screen, star[s].color, (star[s].x, star[s].y), star[s].r)

        s = s + 1


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
    for i in range(s):
        star[i].move()

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
                    for j in range(k):
                        pygame.draw.circle(screen, ball[j].color, (ball[j].x, ball[j].y), ball[j].r)
                    pygame.display.update()
                    break
            for i in range(s):
                if (event.pos[0] - star[i].x) ** 2 + (event.pos[1] - star[i].y) ** 2 <= star[i].r ** 2:  # реализация уничтожение при клике
                    screen.fill(BLACK)

                    score = score + 1  # увеличение счета
                    s = s - 1  # уменьшение количества шариков

                    Text(score)
                    pygame.display.update()
                    # сдвиг всего массива
                    for j in range(i, s):
                        star[j].x = star[j + 1].x
                        star[j].y = star[j + 1].y
                        star[j].r = star[j + 1].r
                        star[j].vx = star[j + 1].vx
                        star[j].vy = star[j + 1].vy
                        star[j].color = star[j + 1].color
                    star.pop(s)
                    # отображение нового набора шаров
                    for j in range(s):
                        pygame.draw.circle(screen, star[j].color, (star[j].x, star[j].y), star[j].r)
                    pygame.display.update()
                    break
    #подготовка к новому начала цикла
    screen.fill(BLACK)
    #добавление на экран и в массив с информацией нового шара

    if a==FPS:
        a=0
        new_ball()



pygame.quit()