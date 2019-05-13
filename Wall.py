import pygame, math
from pygame.locals import *

class Wall(pygame.sprite.Sprite):
    
    def __init__(self, top, bottom, left, right, col):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((right-left, bottom-top)).convert()
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        
