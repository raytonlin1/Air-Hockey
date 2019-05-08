import pygame
from Paddle import *
from Puck import *
from pygame.locals import *
pygame.init()

#screen = pygame.display.set_mode((1000, 640))
screen = pygame.display.set_mode((1040, 700))
p1 = Paddle("redpaddle.png", 1, 100, 10, 690, 520, 60)
p2 = Paddle("bluepaddle.png", 0, 100, 520, 690, 1030, 60)
puck = Puck("puck.png", 100, 10, 690, 1030, 45)
background = pygame.Surface(screen.get_size()).convert()
pygame.display.set_caption('Air Hockey')
background.fill((255, 255, 255))
clock = pygame.time.Clock()

keep_going = True

recSize1 = (10,610)
recSize2 = (1040,10)
# 2 different sizes for goals because of adjustment of goal size in level 1
size1 = 200
size2 = 200
goalSizeLeft = (10,size1)
goalSizeRight = (10,size2)

recSideLeft = pygame.Surface(recSize1).convert()
recSideRight = pygame.Surface(recSize1).convert()
recSideTop = pygame.Surface(recSize2).convert()
recSideBottom = pygame.Surface(recSize2).convert()
goalLeft = pygame.Surface(goalSizeLeft).convert()
goalRight = pygame.Surface(goalSizeRight).convert()

while keep_going:
    clock.tick(60)
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
    goalLeft.fill((0,0,0))
    goalRight.fill((0,0,0))
    puck.update()
    
    screen.blit(background, (0, 0))
    # Centre line of air hockey surface
    pygame.draw.line(screen, (255,0,0), (519,100), (519,690),5)
    # Circles at centre of air hockey surface
    pygame.draw.circle(screen, (255,0,0), (520, 395), 130)
    pygame.draw.circle(screen, (255,255,255), (520, 395), 125)

    # Semicircle at left goal
    pygame.draw.circle(screen, (255,0,0), (0, 400), 120)
    pygame.draw.circle(screen, (255,255,255), (0, 400), 115)

    # Semicircle at right goal
    pygame.draw.circle(screen, (255,0,0), (1040, 400), 120)
    pygame.draw.circle(screen, (255,255,255), (1040, 400), 115)
    screen.blit(p1.image, p1.rect)
    screen.blit(p2.image, p2.rect)
    screen.blit(puck.image, puck.rect)
    screen.blit(recSideLeft, (0,100))
    screen.blit(recSideRight, (1030,100))
    screen.blit(recSideTop, (0,90))
    screen.blit(recSideBottom, (0,690))
    screen.blit(goalLeft, (0,(100+((700-100)/2)-(size1/2))))
    screen.blit(goalRight, (1030,(100+((700-100)/2)-(size2/2))))

    pygame.display.flip()
