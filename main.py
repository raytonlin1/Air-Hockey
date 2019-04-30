import pygame
from Paddle import *
from Puck import *
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1000, 640))
p1 = Paddle("redpaddle.png", 1, 0, 0, 640, 500)
p2 = Paddle("bluepaddle.png", 0, 0, 500, 640, 1000)
puck = Puck("puck.png", 0, 0, 640, 1000)
background = pygame.Surface(screen.get_size()).convert()
pygame.display.set_caption('Air Hockey')
background.fill((255, 255, 255))
clock = pygame.time.Clock()

keep_going = True

while keep_going:
    clock.tick(30)
    for ev in pygame.event.get():
        if ev.type == QUIT:
            keep_going = False
    keys = pygame.key.get_pressed()
    p1.update(keys)
    p2.update(keys)
    screen.blit(background, (0, 0))
    screen.blit(p1.image, p1.rect)
    screen.blit(p2.image, p2.rect)
    screen.blit(puck.image, puck.rect)
    pygame.display.flip()
    # testing
