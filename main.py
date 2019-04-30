import pygame
from Player import *
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640, 640))
p1 = Player(2, 0, 0, 0, 640, 640)
background = pygame.Surface(screen.get_size()).convert()
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
    screen.blit(background, (0, 0))
    screen.blit(p1.image, p1.rect)
    pygame.display.flip()
