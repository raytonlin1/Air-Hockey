import pygame
from pygame.locals import *

class Goal(pygame.sprite.Sprite):

    def __init__(self, id, left, top, width):
        # Constructs the parent component
        pygame.sprite.Sprite.__init__(self)
        # Creates a goal
        self.image = pygame.Surface((55,width)).convert()
        # Colour of goal is black
        self.image.fill((0,0,0))
        # Determines the attributes of the goal as a rectangle
        self.rect = self.image.get_rect()

        # Sets the position of the goal
        self.rect.left = left
        self.rect.top = top
