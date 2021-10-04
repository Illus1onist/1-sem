import pygame
import pygame.draw

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))





pygame.draw.rect(screen, (240, 255, 255), (0, 350, 400, 250))
pygame.draw.rect(screen, (135, 206, 250), (0, 0, 400, 350))
def fish(x,y,o,k):
    pygame.draw.ellipse(screen, (160, 160, 160), (x + 21 * o * k - 20 * k + 20 * o * k, y + 16 * k, 40 * k, 15 * k))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + 21 * o * k - 20 * k + 20 * o * k, y + 16 * k, 40 * k, 15 * k), 1)
    pygame.draw.polygon(screen,(210,0,0),[(x+8*k*o,y+14*k),(x+21*k*o,y+22*k),(x+11*k*o,y+31*k),(x+8*k*o,y+14*k)])
    pygame.draw.polygon(screen, (210, 0, 0), [(x+32*k*o, y+9*k), (x+42*k*o, y+8*k), (x+48*k*o, y+16*k), (x+37*k*o, y+16*k), (x+32*k*o, y+9*k)])
    pygame.draw.polygon(screen, (210, 0, 0), [(x+34*k*o, y+29*k), (x+50*k*o, y+29*k), (x+47*k*o, y+34*k), (x+31*k*o, y+34*k), (x+34*k*o, y+29*k)])
    pygame.draw.circle(screen, (0, 0, 255), (x+52*k*o, y+21*k), 2 * k)

def bear(x,y,k,o):

    pygame.draw.ellipse(screen, (240, 255, 255), (x+100*o*k-50*k+50*o*k,y+300*k,100*k,200*k))
    pygame.draw.ellipse(screen, (0, 0, 0), (x+100*o*k-50*k+50*k*o,y+300*k,100*k,200*k),1)
    pygame.draw.ellipse(screen, (240, 255, 255), (x+140*o*k-35*k+35*o*k,y+270*k,70*k,40*k))
    pygame.draw.ellipse(screen, (0, 0, 0), (x+140*o*k-35*k+35*o*k,y+270*k,70*k,40*k),1)
    pygame.draw.circle(screen, (0,0,0), (x+170*o*k,y+284*k),4*k)
    pygame.draw.circle(screen, (0,0,0), (x+208*o*k,y+288*k),4*k)

    s = pygame.Surface((30*k,200*k),pygame.SRCALPHA)
    s.set_alpha(100)
    pygame.draw.ellipse(s, (0,0,0),(0,0,100*k,200*k),3)
    s2=pygame.transform.rotate(s,-90+45*o)
    screen.blit(s2,(x+190*o*k-80*k+80*o*k,y+190*k))

    pygame.draw.ellipse(screen, (240, 255, 255), (x+163*o*k-40*k+40*o*k,y+338*k,80*k,35*k))
    pygame.draw.ellipse(screen, (0, 0, 0), (x+163*o*k-40*k+40*o*k,y+338*k,80*k,35*k),1)
    pygame.draw.ellipse(screen, (240, 255, 255), (x+140*o*k-40*k+40*o*k,y+450*k,80*k,60*k))
    pygame.draw.ellipse(screen, (0, 0, 0), (x+140*o*k-40*k+40*o*k,y+450*k,80*k,60*k),1)



    pygame.draw.ellipse(screen, (240, 255, 255), (x+183*o*k-30*k+30*o*k,y+487*k,60*k,28*k))
    pygame.draw.ellipse(screen, (0, 0, 0), (x+183*o*k-30*k+30*o*k,y+487*k,60*k,28*k),1)
    pygame.draw.circle(screen, (240, 255, 255), (x+146*o*k,y+274*k),7*k)
    pygame.draw.circle(screen, (0, 0, 0), (x+146*o*k,y+274*k),7*k,1)

    pygame.draw.ellipse(screen, (105, 105, 105), (x+291*o*k-50*k+50*o*k,y+410*k,100*k,45*k))
    pygame.draw.ellipse(screen, (47, 79, 79), (x+301*o*k-40*k+40*o*k,y+425*k,80*k,30*k))

    fish(x + 410 * k * o, y  + 455 * k, -1 * o, 1 * k)
    fish(x + 280 * k * o, y  + 440 * k, 1 * o, 1 * k)
    fish(x + 345 * k * o, y  + 378 * k, -1 * o, 1 * k)
    fish(x + 300 * k * o, y  + 360 * k, 1 * o, 1 * k)
    fish(x + 410 * k * o, y  + 383 * k, -1 * o, 1 * k)

    pygame.draw.line(screen, (0,0,0), (x+341*o*k,y+220*k),(x+341*o*k,y+440*k))

bear(500,100,0.8,-1)
bear(-35,170,0.5,1)
bear(-120,180,0.85,1)


pygame.draw.circle(screen,(240,230,140),(275,105),100)
pygame.draw.circle(screen,(135, 206, 250),(275,105),80)
pygame.draw.circle(screen,(240,230,140),(275,105),20)
pygame.draw.rect(screen, (240,230,140), (180, 97, 190, 20))
pygame.draw.rect(screen, (240,230,140), (265, 18, 20, 180))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)

pygame.quit()