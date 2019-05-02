import pygame
import math
from pygame.locals import *

import random

class Puck(pygame.sprite.Sprite):

    def __init__(self, img, top, left, bottom, right):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        pygame.transform.scale(pygame.image.load(img).convert_alpha(), (30,30), self.image)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (((left+right)/2)-15, ((top+bottom)/2)-15)
        self.id = id
        self.xmin = left
        self.ymin = top
        self.xmax = right
        self.ymax = bottom
        self.vPuckX = 0
        self.vPuckY = 0

    def update(self):
        self.vx -= 1
        self.vy -= 1 
        self.rect.move_ip(self.vx, self.vy)

        # Forms the barrier in which the paddle can move
        # If paddle hits the left barrier
        if self.rect.left<self.xmin:
            # Forms left barrier for each paddle
            self.rect.left = self.xmin
            # When paddle hits the left barrier it stops moving
            self.vx = 0
        # If paddle hits the right barrier
        elif self.rect.right>self.xmax:
            # Forms right barrier for each paddle
            self.rect.right = self.xmax
            # When paddle hits the right barrier it stops moving
            self.vx = 0

        # If paddle hits the top barrier
        if self.rect.top<self.ymin:
            # Forms the top barrier for each paddle
            self.rect.top = self.ymin
            # When paddle hits the top barrier its stops moving
            self.vy = 0
        # If paddle hits the bottom barrier
        elif self.rect.bottom>self.ymax:
            # Forms the bottom barrier for each paddle
            self.rect.bottom = self.ymax
            # When paddle hits the bottom barrier it stops moving
            self.vy = 0    
        
        
