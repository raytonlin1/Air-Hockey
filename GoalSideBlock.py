# Imports the pygame module
import pygame, math
# Imports all local functions from pygame.local
from pygame.locals import *
# Initiates pygame
pygame.init()

class GoalSideBlock(pygame.sprite.Sprite):

    def __init__(self, id, left, top, width):
        # Constructs the parent component
        pygame.sprite.Sprite.__init__(self)
        # Creates a goalSideBlock
        self.image = pygame.Surface((55, width)).convert()
        # Colour of goalSideBlock is brown
        self.image.fill((138, 54, 15))
        # Determines the attributes of the goal as a rectangle
        self.rect = self.image.get_rect()

        # Sets the position of the goal
        self.rect.left = left
        self.rect.top = top
        
