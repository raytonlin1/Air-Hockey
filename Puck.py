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
        self.vPuckX = self.vx
        self.vPuckY = self.vy
        
