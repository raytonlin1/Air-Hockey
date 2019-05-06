import pygame
from Paddle import *
from Puck import *
from pygame.locals import *
pygame.init()

#screen = pygame.display.set_mode((1000, 640))
screen = pygame.display.set_mode((1040, 700))
p1 = Paddle("redpaddle.png", 1, 100, 10, 690, 520, 50)
p2 = Paddle("bluepaddle.png", 0, 100, 520, 690, 1030, 50)
puck = Puck("puck.png", 100, 10, 690, 1030, 30)
background = pygame.Surface(screen.get_size()).convert()
pygame.display.set_caption('Air Hockey')
background.fill((255, 255, 255))
clock = pygame.time.Clock()

keep_going = True

recSize1 = (10,610)
recSize2 = (1040,10)

recSideLeft = pygame.Surface(recSize1).convert()
recSideRight = pygame.Surface(recSize1).convert()
recSideTop = pygame.Surface(recSize2).convert()
recSideBottom = pygame.Surface(recSize2).convert()

while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
    keys = pygame.key.get_pressed()
    p1.update(keys)
    p2.update(keys)
    if (p1.collide(puck)):
        puck.bounce(p1)
    if (p2.collide(puck)):
        puck.bounce(p2)
    recSideLeft.fill((138,54,15))
    recSideRight.fill((138,54,15))
    recSideTop.fill((138,54,15))
    recSideBottom.fill((138,54,15))
    puck.update()
    screen.blit(background, (0, 0))
    screen.blit(p1.image, p1.rect)
    screen.blit(p2.image, p2.rect)
    screen.blit(puck.image, puck.rect)
    screen.blit(recSideLeft, (0,100))
    screen.blit(recSideRight, (1030, 100))
    screen.blit(recSideTop, (0, 90))
    screen.blit(recSideBottom, (0, 690))
    pygame.display.flip()
