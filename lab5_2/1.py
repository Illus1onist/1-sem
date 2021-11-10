import math
import random
import pygame.locals

import pygame

'''
Поворот пушки на q,e и движение на a,d
Поворот второй пушки на 7,9 и движение на 4,6
выстрел из первой - левая конпка мыши.
выстрел из второй - правая.
У таргетов есть вариант, при котором они не двигаются по x совсем, так и задумано! Итак не весело в это играть...


'''



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
    def __init__(self, screen: pygame.Surface, x, y):
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
        "отражает мяч от вертикальных стен и при касании нижней грани рикошетит с уменьшением скорости как по X так и по Y"
        # FIXME
        g=2.0
        self.vy = self.vy - g
        self.x += self.vx
        self.y -= self.vy
        if self.x>=800:
            self.x=800
            self.vx=-self.vx
        if self.x<=0:
            self.x=0
            self.vx=-self.vx
        if self.y>=600-10:
            if abs(self.vx)>=0.1:
                self.vy=-self.vy*0.6
                self.vx=0.7*self.vx
                self.y=600-10
            if abs(self.vx) < 0.1:
                self.live=0

    def draw(self):
        #Рисунок
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

#Класс бомбы, которую кидает таргет. g везде разное, но мне не очень важно)
class Bomb():
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = (0,0,0)
        self.live = 30
    def move(self):

        g=0.05
        self.vy = self.vy - g
        self.y -= self.vy
        if self.y >=  900:
            self.live=0
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.r)

#класс для танка
class Gun:
    def __init__(self, screen,x,y):
        self.bullet=0
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x=x
        self.y=y

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """

        self.bullet += 1
        new_ball = Ball(self.screen,self.x,self.y)
        new_ball.r += 5

        new_ball.vx = self.f2_power * math.cos(self.an)/FPS*20
        new_ball.vy = - self.f2_power * math.sin(self.an)/FPS*20
        self.balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10



    def targetting(self, x):
        """Прицеливание. Зависит от кнопок."""
        self.an=self.an+x*0.05

        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        l=self.f2_power*0.05
        pygame.draw.circle(screen,GREEN,(self.x,self.y),30)
        pygame.draw.polygon(screen, self.color, [(self.x-5*math.sin(self.an),self.y+5*math.cos(self.an)),(-5*math.sin(self.an)+self.x+l*40*math.cos(self.an),self.y+l*40*math.sin(self.an)+5*math.cos(self.an)),(-5*math.sin(self.an)+self.x+40*l*math.cos(self.an)+10*math.sin(self.an),self.y+40*l*math.sin(self.an)-10*math.cos(self.an)+5*math.cos(self.an)),(-5*math.sin(self.an)+self.x+10*math.sin(self.an),self.y-10*math.cos(self.an)+5*math.cos(self.an)),(self.x-5*math.sin(self.an),450+5*math.cos(self.an))])

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
        r = self.r = random.randint(20, 50)
        x = self.x = random.randint(self.r, 800-self.r)
        y = self.y = random.randint(100, 200)

        self.vx= random.randint(-3, 3)
        self.vy = random.randint(-2, 2)
        self.color = color
        self.points = 0
        self.live = 1

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global score
        score=score+1

    #создание бомб
    def tickbomb(self):
        newbomb=Bomb(screen,self.x,self.y)
        self.bombs.append(newbomb)

    #несколько видов движения
    def move1(self):
        g=0.2
        self.vy=self.vy+g
        self.x += self.vx
        self.y -= self.vy
        if self.x >= 800-self.r:
            self.x = 800-self.r
            self.vx = -self.vx
        if self.x <= self.r:
            self.x = self.r
            self.vx = -self.vx

        if self.y <= self.r:
            self.vy = -self.vy
            self.y = self.r
        self.x += self.vx
        self.y -= self.vy
    def move2(self):
        self.x += self.vx
        if self.x >= 800-self.r:
            self.x = 800-self.r
            self.vx = -self.vx
        if self.x <= self.r:
            self.x = self.r
            self.vx = -self.vx
        self.x += self.vx


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


#часы, создание объектов и списков объектов (например для пуль танков и бомб таргетов)
clock = pygame.time.Clock()
gun1 = Gun(screen,40,450)
gun2=   Gun(screen,200,450)
gun1.balls = []
gun2.balls = []

target1 = Target()
target2 = Target()
target1.bombs = []
target2.bombs = []
finished = False
target1.new_target(RED)
target2.new_target(BLUE)

#таймеры и вспомогательные вещи... (немножко магии)
l=0
t=0
timer1=0 #таймер перед появлением новой цели после убитой
timer2=0 #таймер перед появлением новой цели после убитой
timer0=0 #таймер глобальный

#начало великого огромного цикла повторений...
while not finished:
    #рисование пушки и экрана
    screen.fill(WHITE)
    #рисуем танки
    gun1.draw()
    gun2.draw()
    timer0=timer0+1
    #обработка всяких там таймеров... таймер таргета это обратный отсчет с его уничтожения до его респауна на экране. Все это время на экране висит надпись о том, какой вы молодец)
    if timer1!=0:
        timer1=timer1-1
        f = pygame.font.Font(None, 36)
        text = f.render('Oh, you are such a noob... You shot a target 1 with ' + str(l) + ' balls', 1,(180, 0, 0))
        screen.blit(text, (100, 200))
    if timer1==0:
        target1.move1()
        target1.draw()
        l=0

    if timer2!=0:
        timer2=timer2-1
        f = pygame.font.Font(None, 36)
        text = f.render('Oh, you are such a noob... You shot a target 2 with ' + str(t) + ' balls', 1, (180, 0, 0))
        screen.blit(text, (100, 250))
    if timer2==0:
        target2.move2()
        target2.draw()
        t=0
    #рисуем пули
    for b in gun1.balls:
        b.draw()
    for b in gun2.balls:
        b.draw()
    Text()

    #рисование таргетов, если их таймеры истекли
    if timer1==0:
        target1.draw()
    if timer2==0:
        target2.draw()

    # рисуем бомбы
    if timer0 % (2 * FPS) == 0:
        target1.tickbomb()
        target2.tickbomb()
    for i in target1.bombs:
        i.move()
    for i in target2.bombs:
        i.move()

    pygame.display.update()


    #часы и оператор кликов и отжатий мыши (с добавлением points таргетам, чтобы было понятно, )
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # левая кнопка мыши
                gun1.fire2_start(event)
            if event.button == 3:  # правая кнопка мыши
                gun2.fire2_start(event)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # левая кнопка мыши
                gun1.fire2_end(event)
                if timer1==0:
                    target1.points = target1.points + 1
                if timer2==0:
                    target2.points = target2.points + 1
            if event.button == 3:  # правая кнопка мыши
                gun2.fire2_end(event)
                if timer1==0:
                    target1.points = target1.points + 1
                if timer2==0:
                    target2.points = target2.points + 1

        elif pygame.key.get_pressed()[pygame.K_q]:
            gun1.targetting(-1)
        elif pygame.key.get_pressed()[pygame.K_e]:
            gun1.targetting(1)
        elif pygame.key.get_pressed()[pygame.K_a]:
            gun1.x=gun1.x-2
        elif pygame.key.get_pressed()[pygame.K_d]:
            gun1.x = gun1.x + 2

        elif pygame.key.get_pressed()[pygame.K_KP7]:
            gun2.targetting(-1)
        elif pygame.key.get_pressed()[pygame.K_KP9]:
            gun2.targetting(1)
        elif pygame.key.get_pressed()[pygame.K_KP4]:
            gun2.x=gun2.x-2
        elif pygame.key.get_pressed()[pygame.K_KP6]:
            gun2.x = gun2.x + 2





    # перебор всех пуль на экране для их движения и проверки столкновений
    s=0
    for b in gun1.balls:
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
        if (b.x-gun2.x)**2+(b.y-gun2.y)**2<=50**2:
            finished=True


        if b.live==0:
            del gun1.balls[s-1]
    gun1.power_up()

    s = 0
    for b in gun2.balls:
        s = s + 1
        b.move()

        # обработка столкновения для обоих целей
        if timer1 == 0 and b.hittest(target1) and target1.live:
            target1.live = 0
            target1.hit()
            l = target1.points
            target1.new_target(RED)
            timer1 = 3 * FPS

        if timer2 == 0 and b.hittest(target2) and target2.live:
            target2.live = 0
            target2.hit()
            t = target2.points
            target2.new_target(BLUE)
            timer2 = 3 * FPS

        if (b.x-gun1.x)**2+(b.y-gun1.y)**2<=50**2:
            finished=True

        if b.live == 0:
            del gun2.balls[s - 1]
    gun2.power_up()
    s = 0

    # перебор всех пуль на экране для их движения и проверки столкновений
    for b in target1.bombs:
        s=s+1
        if (b.x-gun1.x)**2+(b.y-gun1.y)**2<=40**2:
            finished=True
        if (b.x-gun2.x)**2+(b.y-gun2.y)**2<=40**2:
            finished=True
        if b.live == 0:
            del target1.bombs[s - 1]
    s = 0
    for b in target2.bombs:
        s=s+1
        if b.live == 0:
            del target2.bombs[s - 1]


pygame.quit()