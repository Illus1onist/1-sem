import math
import random

import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

global score
score=0

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = random.choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        g=2.5
        self.vy = self.vy - g
        self.x += self.vx
        self.y -= self.vy
        if self.x>=800:
            self.x=self.x-20
            self.vx=-self.vx
        if self.x<=0:
            self.x=self.x+20
            self.vx=-self.vx
        if self.y>=600-10:
            if abs(self.vx)>=2:
                self.vy=-self.vy*0.6
                self.vx=0.7*self.vx
                self.y=599-10
            if abs(self.vx) < 2:
                self.live=0

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if (self.x-obj.x)**2+(self.y-obj.y)**2>=(obj.r+self.r)**2:
            return False
        else:
            return True


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)/FPS*20
        new_ball.vy = - self.f2_power * math.sin(self.an)/FPS*20
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        l=self.f2_power*0.05
        pygame.draw.polygon(screen, self.color, [(40,450),(40+l*40*math.cos(self.an),450+l*40*math.sin(self.an)),(40+40*l*math.cos(self.an)+10*math.sin(self.an),450+40*l*math.sin(self.an)-10*math.cos(self.an)),(40+10*math.sin(self.an),450-10*math.cos(self.an)),(40,450)])

        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:

    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()


    def new_target(self,color):
        """ Инициализация новой цели. """
        x = self.x = random.randint(600, 780)
        y = self.y = random.randint(300, 550)
        r = self.r = random.randint(2, 50)
        self.color = color
        self.points = 0
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global score
        score=score+1


    def draw(self):

        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)

#счет
def Text():
    f = pygame.font.Font(None, 36)
    text = f.render('Score:' + str(score), 1, (180, 0, 0))
    screen.blit(text, (250, 20))



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

#часы, создание объектов
clock = pygame.time.Clock()
gun = Gun(screen)
target1 = Target()
target2 = Target()
finished = False
target1.new_target(RED)
target2.new_target(BLUE)

#таймеры и вспомогательные вещи... (немножко магии)
l=0
t=0
timer1=0
timer2=0
#начало великого огромного цикла повторений...
while not finished:
    #рисование пушки и экрана
    screen.fill(WHITE)
    gun.draw()

    #обработка всяких там таймеров... таймер таргета это обратный отсчет с его уничтожения до его респауна на экране. Все это время на экране висит надпись о том, какой вы молодец)
    if timer1!=0:
        timer1=timer1-1
        f = pygame.font.Font(None, 36)
        text = f.render('Oh, you are such a noob... You shot a target 1 with ' + str(l) + ' balls', 1,(180, 0, 0))
        screen.blit(text, (100, 200))
    if timer1==0:
        target1.draw()
        l=0

    if timer2!=0:
        timer2=timer2-1
        f = pygame.font.Font(None, 36)
        text = f.render('Oh, you are such a noob... You shot a target 2 with ' + str(t) + ' balls', 1, (180, 0, 0))
        screen.blit(text, (100, 250))
    if timer2==0:
        target2.draw()
        t=0

    for b in balls:
        b.draw()
    Text()

    #рисование таргетов, если их таймеры истекли
    if timer1==0:
        target1.draw()
    if timer2==0:
        target2.draw()

    pygame.display.update()


    #часы и оператор кликов и отжатий мыши (с добавлением points таргетам, чтобы было понятно, )
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
            if timer1==0:
                target1.points = target1.points + 1
            if timer2==0:
                target2.points = target2.points + 1
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    # перебор всех шариков на экране для их движения и проверки столкновений
    s=0
    for b in balls:
        s=s+1
        b.move()

        #обработка столкновения для обоих целей
        if timer1==0 and b.hittest(target1) and target1.live:

            target1.live = 0
            target1.hit()
            l=target1.points
            target1.new_target(RED)
            timer1=3*FPS


        if timer2==0 and b.hittest(target2) and target2.live:

            target2.live = 0
            target2.hit()
            t=target2.points
            target2.new_target(BLUE)
            timer2=3*FPS


        if b.live==0:
            del balls[s-1]
    gun.power_up()


pygame.quit()